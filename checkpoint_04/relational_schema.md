# Bits & Books: final relational schema

`#` marks a primary-key column; `FK` marks a foreign key. Foreign keys are part of a primary key only in the two junction tables. The authoritative column types and constraints are in `schema.sql`.

- **Publisher** (`PublisherID`#, Name)
- **Book** (`ISBN`#, Title, PublicationYear, StockQuantity, Price, BPublisherID FK → Publisher.PublisherID)
- **Author** (`AuthorID`#, Bio, FirstName, MiddleName, LastName)
- **Category** (`CategoryID`#, CategoryName, Description)
- **Customer** (`CustomerID`#, FirstName, LastName, Email, Phone, Street, City, State, ZIPCode)
- **Employee** (`EmployeeID`#, FirstName, LastName, Email, Phone, Position, HourlyRate)
- **Orders** (`OrderID`#, OrderDate, PaymentMethod, OrderStatus, OCustomerID FK → Customer.CustomerID, OEmployeeID FK → Employee.EmployeeID)
- **Order_Item** (`OrderItemID`#, Quantity, UnitPrice, OOrderID FK → Orders.OrderID, OISBN FK → Book.ISBN)
- **BookRating** (`RatingID`#, Rating, RISBN FK → Book.ISBN, RCustomerID FK → Customer.CustomerID); UNIQUE (RCustomerID, RISBN).
- **Writes** (`WISBN`# FK → Book.ISBN, `WAuthorID`# FK → Author.AuthorID); composite primary key (WISBN, WAuthorID).
- **Is_In** (`IISBN`# FK → Book.ISBN, `ICategoryID`# FK → Category.CategoryID); composite primary key (IISBN, ICategoryID).

ISBN is the book key; redundant BookID was removed. The supplied CSV gives a year, so PublicationYear is an INTEGER rather than a fabricated full date. MiddleName holds all name parts between the first and last, which handles the supplied CSV but is not a general solution for every possible naming convention. Orders is used consistently as the SQL table name. OrderPrice is derived as SUM(Quantity * UnitPrice).

Each book has one publisher, each order one customer, each order item one order and book, and each rating one customer and book. Employee assignment is optional. Writes and Is_In represent many-to-many links. The business rule that a book has at least one author and an order at least one item requires application or transaction-level validation; a foreign key alone does not enforce a minimum number of dependent rows. The loaded data meets both rules.

`schema.sql` states checks, uniqueness, and all referenced columns and ON DELETE/UPDATE rules next to their definitions. Book and customer deletion is restricted when purchase history or ratings refer to them; removing an order cascades to its items; removing an employee sets the order's employee to NULL; book/author and book/category junction links cascade when their parent is deleted. Enable `PRAGMA foreign_keys = ON` for every SQLite connection.
