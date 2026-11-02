import csv, sqlite3, pathlib

BASE = pathlib.Path(__file__).resolve().parent
DB = BASE / "bits_and_books.db"
if DB.exists(): DB.unlink()
con = sqlite3.connect(DB)
con.execute("PRAGMA foreign_keys=ON")
con.executescript((BASE / "schema.sql").read_text())

# The source CSV stores coauthors on following rows with a blank ISBN.
books=[]; authors=[]
with (BASE / "Proj Data Unix.csv").open(encoding="cp1252", newline="") as f:
    rows=list(csv.reader(f))
for row in rows[2:]:
    if len(row)<7: continue
    if row[0].strip():
        isbn,title,author,publisher,year,price,category=(x.strip() for x in row[:7])
        if not isbn: continue
        authors=[author] if author else []
        books.append((isbn,title,publisher,year,price,category,authors))
    elif row[2].strip() and books:
        books[-1][6].append(row[2].strip())

# Seed publisher, author, category and book rows from source records.
for isbn,title,publisher,year,price,category,book_authors in books:
    pub=con.execute("SELECT PublisherID FROM Publisher WHERE Name=?",(publisher,)).fetchone()
    if pub is None: con.execute("INSERT INTO Publisher(Name) VALUES(?)",(publisher,)); pub=con.execute("SELECT PublisherID FROM Publisher WHERE Name=?",(publisher,)).fetchone()
    cat=con.execute("SELECT CategoryID FROM Category WHERE CategoryName=?",(category,)).fetchone()
    if cat is None: con.execute("INSERT INTO Category(CategoryName) VALUES(?)",(category,)); cat=con.execute("SELECT CategoryID FROM Category WHERE CategoryName=?",(category,)).fetchone()
    pid,cid=pub[0],cat[0]
    if con.execute("SELECT 1 FROM Book WHERE ISBN=?",(isbn,)).fetchone(): continue
    stock=2 if isbn in {books[0][0], books[1][0], books[2][0]} else 12
    con.execute("INSERT INTO Book(ISBN,Title,PublicationDate,StockQuantity,Price,BPublisherID) VALUES(?,?,?,?,?,?)",(isbn,title,year+'-01-01',stock,float(price.replace('$','').replace(',','')),pid))
    con.execute("INSERT INTO Is_In(IISBN,ICategoryID) VALUES(?,?)",(isbn,cid))
    for full in book_authors:
        parts=full.split()
        if not parts: continue
        first,last=parts[0],parts[-1]
        author=con.execute("SELECT AuthorID FROM Author WHERE FirstName=? AND LastName=?",(first,last)).fetchone()
        if author is None: con.execute("INSERT INTO Author(FirstName,LastName) VALUES(?,?)",(first,last)); author=con.execute("SELECT AuthorID FROM Author WHERE FirstName=? AND LastName=?",(first,last)).fetchone()
        aid=author[0]
        con.execute("INSERT OR IGNORE INTO Writes(WISBN,WAuthorID) VALUES(?,?)",(isbn,aid))

# Related sample rows support the customer/order query cases.
customers=[("Avery","Reader","email_example"),("Blair","Reader","blair@example.com"),("Casey","Reader","casey@example.com")]
for fn,ln,email in customers:
    con.execute("INSERT INTO Customer(FirstName,LastName,Email) VALUES(?,?,?)",(fn,ln,email))
con.execute("INSERT INTO Employee(FirstName,LastName,Email,Position,HourlyRate) VALUES('Morgan','Staff','morgan@example.com','Fulfillment',20.00)")
customer_ids={email:con.execute("SELECT CustomerID FROM Customer WHERE Email=?",(email,)).fetchone()[0] for _,_,email in customers}
employee_id=con.execute("SELECT EmployeeID FROM Employee WHERE Email='morgan@example.com'").fetchone()[0]
# Pick the six supplied Pratchett books, and one other catalog title.
terry=con.execute("SELECT B.ISBN FROM Book B JOIN Writes W ON B.ISBN=W.WISBN JOIN Author A ON A.AuthorID=W.WAuthorID WHERE A.FirstName='Terry' AND A.LastName='Pratchett' ORDER BY B.Title").fetchall()
other=con.execute("SELECT ISBN FROM Book WHERE ISBN NOT IN (SELECT WISBN FROM Writes JOIN Author ON Writes.WAuthorID=Author.AuthorID WHERE FirstName='Terry' AND LastName='Pratchett') ORDER BY Title LIMIT 1").fetchone()
selections=[(customer_ids['email_example'],'2026-10-01',terry[0][0],2),(customer_ids['email_example'],'2026-10-15',terry[1][0],1),(customer_ids['blair@example.com'],'2026-10-18',terry[2][0],1),(customer_ids['casey@example.com'],'2026-10-20',other[0],3)]
for cid,date,isbn,qty in selections:
    cur=con.execute("INSERT INTO Orders(OrderDate,PaymentMethod,OrderStatus,OCustomerID,OEmployeeID) VALUES(?,?,?,?,?)",(date,'Credit Card','Delivered',cid,employee_id))
    price=con.execute("SELECT Price FROM Book WHERE ISBN=?",(isbn,)).fetchone()[0]
    con.execute("INSERT INTO Order_Item(Quantity,UnitPrice,OOrderID,OISBN) VALUES(?,?,?,?)",(qty,price,cur.lastrowid,isbn))
con.execute("INSERT INTO BookRating(Rating,RISBN,RCustomerID) VALUES(5,?,?)",(terry[0][0],customer_ids['email_example']))
con.commit(); con.close()
