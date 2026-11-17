"""Build a new demonstration database from the supplied CSV; never overwrite a file."""
import csv
import sqlite3
import sys
from pathlib import Path

BASE = Path(__file__).resolve().parent
if len(sys.argv) != 2:
    raise SystemExit('Usage: python3 etl.py /path/to/new-database.sqlite')
path = Path(sys.argv[1]).resolve()
if path.exists():
    raise SystemExit(f'Refusing to overwrite {path}')
con = sqlite3.connect(path)
con.execute('PRAGMA foreign_keys = ON')
con.executescript((BASE / 'schema.sql').read_text())

def get_id(table, column, name):
    idcol = {'Publisher':'PublisherID', 'Category':'CategoryID'}[table]
    row = con.execute(f'SELECT {idcol} FROM {table} WHERE {column}=?', (name,)).fetchone()
    if row: return row[0]
    return con.execute(f'INSERT INTO {table} ({column}) VALUES (?)', (name,)).lastrowid

def add_author(isbn, full):
    for name in (x.strip() for x in full.split(',')):
        if not name: continue
        parts = name.split()
        if len(parts) < 2: raise ValueError(f'Author name cannot be split: {name}')
        first, last, middle = parts[0], parts[-1], ' '.join(parts[1:-1]) or None
        author = con.execute('SELECT AuthorID FROM Author WHERE FirstName=? AND MiddleName IS ? AND LastName=?', (first,middle,last)).fetchone()
        aid = author[0] if author else con.execute('INSERT INTO Author(FirstName,MiddleName,LastName) VALUES(?,?,?)', (first,middle,last)).lastrowid
        con.execute('INSERT OR IGNORE INTO Writes VALUES(?,?)', (isbn,aid))

with (BASE / 'source_catalog.csv').open(encoding='cp1252', newline='') as f:
    rows = list(csv.reader(f))
current = None
for row in rows[2:]:
    if len(row) < 7: continue
    isbn,title,authors,publisher,year,price,category = (x.strip() for x in row[:7])
    if isbn:
        current = isbn
        pid = get_id('Publisher','Name',publisher)
        cid = get_id('Category','CategoryName',category)
        con.execute('INSERT OR IGNORE INTO Book(ISBN,Title,PublicationYear,StockQuantity,Price,BPublisherID) VALUES(?,?,?,?,?,?)', (isbn,title,int(year),12,float(price.replace('$','').replace(',','')),pid))
        con.execute('INSERT OR IGNORE INTO Is_In VALUES(?,?)', (isbn,cid))
    if authors:
        if current is None: raise ValueError('Author continuation before a book')
        add_author(current,authors)

# All sales, customers, ratings, stock levels, and employees are invented test data.
customers = [ ('Avery','Reader','avery.reader@example.com','614-555-0101','Columbus','OH'), ('Casey','Morgan','casey.morgan@example.com','614-555-0102','Columbus','OH'), ('Blair','Reed','blair.reed@example.com','614-555-0103','Dublin','OH'), ('Dana','Lee','dana.lee@example.com','614-555-0104','Westerville','OH') ]
for first,last,email,phone,city,state in customers:
    con.execute('INSERT INTO Customer(FirstName,LastName,Email,Phone,City,State) VALUES(?,?,?,?,?,?)',(first,last,email,phone,city,state))
con.execute("INSERT INTO Employee(FirstName,LastName,Email,Position,HourlyRate) VALUES('Morgan','Staff','morgan.staff@example.com','Fulfillment',20)")
terry = [r[0] for r in con.execute("SELECT b.ISBN FROM Book b JOIN Writes w ON w.WISBN=b.ISBN JOIN Author a ON a.AuthorID=w.WAuthorID WHERE a.FirstName='Terry' AND a.LastName='Pratchett' ORDER BY b.Title")]
other = [r[0] for r in con.execute("SELECT ISBN FROM Book WHERE ISBN NOT IN (SELECT WISBN FROM Writes JOIN Author ON WAuthorID=AuthorID WHERE FirstName='Terry' AND LastName='Pratchett') ORDER BY Title LIMIT 4")]
con.execute('UPDATE Book SET StockQuantity=0 WHERE ISBN=?',(terry[0],))
con.execute('UPDATE Book SET StockQuantity=2 WHERE ISBN=?',(terry[1],))
con.execute('UPDATE Book SET StockQuantity=4 WHERE ISBN=?',(other[0],))
orders = [ (1,'2026-10-01','Credit Card','Delivered',[(terry[0],2),(other[0],1)]), (1,'2026-10-15','PayPal','Shipped',[(terry[1],2)]), (2,'2026-10-02','Debit Card','Delivered',[(terry[2],3),(other[1],2)]), (3,'2026-10-18','Gift Card','Processing',[(terry[0],1),(other[2],1)]) ]
for customer,date,payment,status,items in orders:
    oid=con.execute('INSERT INTO Orders(OrderDate,PaymentMethod,OrderStatus,OCustomerID,OEmployeeID) VALUES(?,?,?,?,1)',(date,payment,status,customer)).lastrowid
    for isbn,qty in items:
        price=con.execute('SELECT Price FROM Book WHERE ISBN=?',(isbn,)).fetchone()[0]
        con.execute('INSERT INTO Order_Item(Quantity,UnitPrice,OOrderID,OISBN) VALUES(?,?,?,?)',(qty,price,oid,isbn))
con.execute('INSERT INTO BookRating(Rating,RISBN,RCustomerID) VALUES(5,?,1)',(terry[0],))
con.execute('INSERT INTO BookRating(Rating,RISBN,RCustomerID) VALUES(4,?,2)',(terry[2],))
con.commit()
assert not con.execute('PRAGMA foreign_key_check').fetchall()
for table in ('Book','Author','Writes','Publisher','Category','Is_In','Customer','Employee','Orders','Order_Item','BookRating'):
    print(table,con.execute(f'SELECT COUNT(*) FROM {table}').fetchone()[0])
con.close()
