# Relational Schema: Bits & Books

**Notation:** `#` = primary key, `FK` = foreign key. Composite primary keys are marked with `#` on every attribute in the key. Underlined primary keys from the ERD are shown with `#`.

---

## Tables

### Book
**Book (ISBN#, BookID, Title, PublicationDate, StockQuantity, Price, BPublisherID#FK)**

- Foreign Key BPublisherID references Publisher
- Data types: ISBN – VARCHAR(13), BookID – INT (UNIQUE), Title – VARCHAR(200), PublicationDate – DATE, StockQuantity – INT, Price – DECIMAL(10,2), BPublisherID – INT (NOT NULL)

### Publisher
**Publisher (PublisherID#, Name)**

- Data types: PublisherID – INT, Name – VARCHAR(100)

### Author
**Author (AuthorID#, Bio, FirstName, LastName)**

- Data types: AuthorID – INT, Bio – TEXT, FirstName – VARCHAR(30), LastName – VARCHAR(30)

### Category
**Category (CategoryID#, CategoryName, Description)**

- Data types: CategoryID – INT, CategoryName – VARCHAR(30), Description – TEXT

### BookRating
**BookRating (RatingID#, Rating, RISBN#FK, RCustomerID#FK)**

- Foreign Key RISBN references Book
- Foreign Key RCustomerID references Customer
- Data types: RatingID – INT, Rating – INT (CHECK between 1 and 5), RISBN – VARCHAR(13) (NOT NULL), RCustomerID – INT (NOT NULL)

### Customer
**Customer (CustomerID#, FirstName, LastName, Email, Phone, Street, City, State, ZIPCode)**

- Data types: CustomerID – INT, FirstName – VARCHAR(30), LastName – VARCHAR(30), Email – VARCHAR(80), Phone – VARCHAR(20), Street – VARCHAR(80), City – VARCHAR(50), State – VARCHAR(30), ZIPCode – VARCHAR(10)

### Order
**Order (OrderID#, OrderDate, PaymentMethod, OrderStatus, OCustomerID#FK, OEmployeeID#FK)**

- Foreign Key OCustomerID references Customer
- Foreign Key OEmployeeID references Employee
- Data types: OrderID – INT, OrderDate – DATE, PaymentMethod – VARCHAR(30), OrderStatus – VARCHAR(30), OCustomerID – INT (NOT NULL), OEmployeeID – INT (NULL allowed)
- OrderPrice is a derived attribute in the ERD, so it is not stored. It is computed as SUM(Quantity × UnitPrice) over the order's items.
- `Order` is a reserved word in SQL, so use `Orders` (or quote the name) when creating the table.

### Employee
**Employee (EmployeeID#, FirstName, LastName, Email, Phone, Position, HourlyRate)**

- Data types: EmployeeID – INT, FirstName – VARCHAR(30), LastName – VARCHAR(30), Email – VARCHAR(80), Phone – VARCHAR(20), Position – VARCHAR(50), HourlyRate – DECIMAL(8,2)

### Order_Item
**Order_Item (OrderItemID#, Quantity, UnitPrice, OOrderID#FK, OISBN#FK)**

- Foreign Key OOrderID references Order
- Foreign Key OISBN references Book
- Data types: OrderItemID – INT, Quantity – INT (CHECK > 0), UnitPrice – DECIMAL(10,2), OOrderID – INT (NOT NULL), OISBN – VARCHAR(13) (NOT NULL)

### Writes (junction table for Book and Author)
**Writes (WISBN#FK, WAuthorID#FK)**

- Composite primary key (WISBN, WAuthorID)
- Foreign Key WISBN references Book
- Foreign Key WAuthorID references Author
- Data types: WISBN – VARCHAR(13), WAuthorID – INT

### Is_In (junction table for Book and Category)
**Is_In (IISBN#FK, ICategoryID#FK)**

- Composite primary key (IISBN, ICategoryID)
- Foreign Key IISBN references Book
- Foreign Key ICategoryID references Category
- Data types: IISBN – VARCHAR(13), ICategoryID – INT

---

## Design Decisions

### Many-to-many relationships
WRITES (Book and Author) and IS_IN (Book and Category) are both many-to-many, so each one became its own table: **Writes** and **Is_In**. Each junction table's primary key is the combination of its two foreign keys, which prevents the same pairing from being stored twice. A book can have many authors and categories, and an author or category can be linked to many books.

### Surrogate keys
Every entity table except Book uses a surrogate key: a system-generated integer ID (auto-increment) with no real-world meaning. This covers Employee, Customer, Order, Order_Item, Publisher, Author, Category and BookRating. Names, emails and addresses are not guaranteed to be unique and can change, so a surrogate key lets each row be found and referenced reliably. Book instead uses the natural key ISBN, since it is a real-world unique identifier for a book, and BookID is kept as a UNIQUE alternate key. Writes and Is_In use composite keys made of their foreign keys.

### Mapping choices
- One-to-many relationships are represented by a foreign key on the "many" side (PLACES, PROCESSES, CONTAINS, GIVES, ABOUT, PUBLISHED_BY).
- Composite attributes (Customer Address, Author Name) are split into atomic columns.
- A 1..1 participation in the ERD became a NOT NULL foreign key. PROCESSES is 0..1, so Order.OEmployeeID allows NULL, meaning an order can be unassigned.

---

## Constraints and Assumptions

### Keys and relationships
- Every foreign key references a primary key that exists, and every entity that needs a primary key has one.
- ISBN uniquely identifies a book. Each edition or format has its own ISBN.
- Every order is placed by a customer who is in the system, so there are no guest orders.
- An order may be unassigned to an employee (OEmployeeID is NULL), for example an order not yet processed.
- Every book has exactly one publisher.
- Every book has at least one author, and every order has at least one item. A plain foreign key cannot enforce a minimum count, so the application or a transaction enforces these.
- Every order item refers to exactly one book through OISBN.

### Data and values
- All prices are in a single currency (USD).
- Order_Item.UnitPrice stores the price at the time of sale, so later changes to Book.Price do not change past orders.
- Quantity is greater than 0, Price is at least 0, StockQuantity is at least 0, and Rating is between 1 and 5.
- PaymentMethod and OrderStatus come from a fixed set of values (for example Pending, Shipped, Delivered, Cancelled).
- Email is unique for each customer and each employee.
- Phone is stored as text, since it may include symbols or leading zeros.
- Each customer has one address, stored in the Customer table.

### Integrity and design
- Deleting a customer, book or publisher that is referenced elsewhere is blocked (RESTRICT) to preserve history. Deleting an order cascades to its order items, and deleting a book or author cascades to the junction rows.
- If an employee is removed, their orders remain and OEmployeeID is set to NULL.
- All attributes are atomic (first normal form). City, State and ZIPCode stay together in Customer for simplicity, even though ZIPCode determines city and state.
- A customer may rate the same book more than once, unless a UNIQUE (RCustomerID, RISBN) constraint is added.
