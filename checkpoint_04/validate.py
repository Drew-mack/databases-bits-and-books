"""Read-only checks of CSV relationships, all 14 query results, and constraints."""
import csv, re, sqlite3
from collections import defaultdict
from pathlib import Path
p=Path(__file__).resolve().parent
c=sqlite3.connect(f'file:{p / "database.sqlite"}?mode=ro',uri=True)
c.row_factory=sqlite3.Row
assert c.execute('PRAGMA integrity_check').fetchone()[0]=='ok'
assert not c.execute('PRAGMA foreign_key_check').fetchall()
# Independently read the CSV's complete book-author and book-category pairs.
source_authors=set(); source_cats=set(); current=None
with (p/'source_catalog.csv').open(encoding='cp1252',newline='') as f: rows=list(csv.reader(f))
for row in rows[2:]:
 if len(row)<7: continue
 isbn,title,authors,publisher,year,price,cat=(v.strip() for v in row[:7])
 if isbn: current=isbn; source_cats.add((isbn,cat))
 if authors:
  for author in authors.split(','):
   if author.strip(): source_authors.add((current,' '.join(author.split())))
db_authors={(r['WISBN'],' '.join(x for x in (r['FirstName'],r['MiddleName'],r['LastName']) if x)) for r in c.execute('SELECT * FROM Writes JOIN Author ON WAuthorID=AuthorID')}
db_cats={(r['IISBN'],r['CategoryName']) for r in c.execute('SELECT * FROM Is_In JOIN Category ON ICategoryID=CategoryID')}
assert db_authors==source_authors, (source_authors-db_authors,db_authors-source_authors)
assert db_cats==source_cats
print('CSV relationship matches:',len(source_authors),'authors,',len(source_cats),'categories')
books={r['ISBN']:dict(r) for r in c.execute('SELECT * FROM Book')}
authors={r['AuthorID']:dict(r) for r in c.execute('SELECT * FROM Author')}
customers={r['CustomerID']:dict(r) for r in c.execute('SELECT * FROM Customer')}
links=defaultdict(set)
for r in c.execute('SELECT * FROM Writes'): links[r['WISBN']].add(r['WAuthorID'])
orders={r['OrderID']:dict(r) for r in c.execute('SELECT * FROM Orders')}
items=[dict(r) for r in c.execute('SELECT * FROM Order_Item')]
terry={i for i,a in authors.items() if a['FirstName']=='Terry' and a['LastName']=='Pratchett'}
counts={cid:0 for cid in customers}; cents={cid:0 for cid in customers}; bookqty=defaultdict(int); bookmoney=defaultdict(int); authqty=defaultdict(int); authmoney=defaultdict(int)
for i in items:
 cid=orders[i['OOrderID']]['OCustomerID']; q=i['Quantity']; money=round(i['UnitPrice']*100)*q; isbn=i['OISBN']
 counts[cid]+=q; cents[cid]+=money; bookqty[isbn]+=q; bookmoney[isbn]+=money
 for aid in links[isbn]: authqty[aid]+=q; authmoney[aid]+=money
high={cid for cid in customers if cents[cid]*len(customers)>sum(cents.values())}
top_a={aid for aid in authors if authmoney[aid]==max(authmoney.values())}
def person(cid):
 x=customers[cid];return (cid,x['FirstName'],x['LastName'])
def author(aid):
 x=authors[aid];return (aid,x['FirstName'],x['MiddleName'],x['LastName'])
expected={
 'a':{(b['Title'],) for isbn,b in books.items() if links[isbn]&terry and b['Price']<10},
 'b':{(books[i['OISBN']]['Title'],orders[i['OOrderID']]['OrderDate']) for i in items if orders[i['OOrderID']]['OCustomerID']==1},
 'c':{(b['Title'],isbn) for isbn,b in books.items() if b['StockQuantity']<5},
 'd':{person(orders[i['OOrderID']]['OCustomerID'])+(books[i['OISBN']]['Title'],) for i in items if links[i['OISBN']]&terry},
 'e':{person(1)+(counts[1],)},
 'f':{person(cid)+(q,) for cid,q in counts.items() if q==max(counts.values())},
 'g':{person(cid)+(v/100,) for cid,v in cents.items()},
 'h':{person(cid)+(cents[cid]/100,) for cid in high},
 'i':{(isbn,b['Title'],bookqty[isbn]) for isbn,b in books.items()},
 'j':{(isbn,b['Title'],bookmoney[isbn]/100) for isbn,b in books.items()},
 'k':{author(aid)+(authqty[aid],) for aid in authors if authqty[aid]==max(authqty.values())},
 'l':{author(aid)+(authmoney[aid]/100,) for aid in authors if authmoney[aid]==max(authmoney.values())},
 'm':{person(orders[i['OOrderID']]['OCustomerID']) for i in items if links[i['OISBN']]&top_a},
 'n':{author(aid) for i in items if orders[i['OOrderID']]['OCustomerID'] in high for aid in links[i['OISBN']]},
}
parts=re.split(r'-- \(([a-n])\) ([^\n]+)\n',(p/'queries.sql').read_text())
for letter,title,sql in zip(parts[1::3],parts[2::3],parts[3::3]):
 rows=[tuple(r) for r in c.execute(sql.strip())]; actual=set(rows)
 assert actual==expected[letter],(letter,actual-expected[letter],expected[letter]-actual)
 assert len(rows)==len(actual), f'duplicate results in {letter}'
 if letter in 'ij':
  vals=[r[2] for r in rows]; assert vals==sorted(vals,reverse=True)
 print(letter,len(rows),'rows matched independent computation')
assert len([v for v in counts.values() if v==max(counts.values())])>=2
assert c.execute('SELECT COUNT(*) FROM Book b WHERE NOT EXISTS (SELECT 1 FROM Writes w WHERE w.WISBN=b.ISBN)').fetchone()[0]==0
assert c.execute('SELECT COUNT(*) FROM Orders o WHERE NOT EXISTS (SELECT 1 FROM Order_Item i WHERE i.OOrderID=o.OrderID)').fetchone()[0]==0
print('Ties and minimum related rows validated.')

# A separate in-memory dataset exercises ties in both author rankings and buyers.
t=sqlite3.connect(':memory:');t.execute('PRAGMA foreign_keys=ON');t.executescript((p/'schema.sql').read_text())
t.executescript("""
INSERT INTO Publisher VALUES (1,'Test publisher');
INSERT INTO Book VALUES ('A','Book A',2020,1,10,1),('B','Book B',2020,1,10,1);
INSERT INTO Author(AuthorID,FirstName,LastName) VALUES (1,'Alice','Author'),(2,'Bob','Author');
INSERT INTO Writes VALUES ('A',1),('B',2);
INSERT INTO Customer(CustomerID,FirstName,LastName,Email) VALUES (1,'A','Buyer','a@example.com'),(2,'B','Buyer','b@example.com'),(3,'C','Buyer','c@example.com');
INSERT INTO Orders(OrderID,OrderDate,PaymentMethod,OrderStatus,OCustomerID) VALUES (1,'2026-01-01','Cash','Delivered',1),(2,'2026-01-01','Cash','Delivered',2);
INSERT INTO Order_Item(Quantity,UnitPrice,OOrderID,OISBN) VALUES (2,10,1,'A'),(2,10,2,'B');
INSERT INTO BookRating(Rating,RISBN,RCustomerID) VALUES (4,'A',1);
""")
queries={letter:sql.strip() for letter,title,sql in zip(parts[1::3],parts[2::3],parts[3::3])}
assert {r[0] for r in t.execute(queries['f'])}=={1,2}
assert {r[0] for r in t.execute(queries['k'])}=={1,2}
assert {r[0] for r in t.execute(queries['l'])}=={1,2}
assert {r[0] for r in t.execute(queries['m'])}=={1,2}
assert {r[0] for r in t.execute(queries['n'])}=={1,2}
try: t.execute("INSERT INTO BookRating(Rating,RISBN,RCustomerID) VALUES(5,'A',1)")
except sqlite3.IntegrityError: pass
else: raise AssertionError('Duplicate customer/book rating accepted')
print('Synthetic buyer and author ties, high-spender author links, and rating uniqueness passed.')
