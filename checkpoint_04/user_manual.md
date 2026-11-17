# Bits & Books Database – User Manual

**Version:** 1.0  
**Last Updated:** November 17, 2026  
**Database Engine:** SQLite  

---

## 1. Introduction

The Bits & Books database supports the daily operations of an online bookstore. It stores information about books, authors, publishers, customers, employees, orders, and ratings. The design uses primary keys, foreign keys, and check constraints to maintain data integrity and realistic relationships between entities.

This manual explains every table, its attributes, and how to safely add or remove records. The catalog originates in the supplied CSV; customers, orders, employees, ratings, and stock levels are demonstration data. Examples use illustrative IDs and ISBNs; check that referenced rows exist in your database.

---

## 2. Table Descriptions & Real-World Mappings

### 2.1 Publisher
**Real-world entity:** A publishing company that releases books (e.g., HarperCollins, Penguin Random House).

| Attribute     | Data Type      | Constraints                          | Description |
|---------------|----------------|--------------------------------------|-------------|
| PublisherID   | INTEGER        | PRIMARY KEY, AUTOINCREMENT           | Unique identifier for the publisher |
| Name          | VARCHAR(100)   | NOT NULL                             | Official name of the publishing company |

### 2.2 Book
**Real-world entity:** An individual book title available for sale in the store.

| Attribute        | Data Type      | Constraints                                      | Description |
|------------------|----------------|--------------------------------------------------|-------------|
| ISBN             | VARCHAR(13)    | PRIMARY KEY                                      | International Standard Book Number (unique identifier) |
| Title            | VARCHAR(200)   | NOT NULL                                         | Full title of the book |
| PublicationYear  | INTEGER        | —                                                | Year the book was published; the source does not supply a full date |
| StockQuantity    | INTEGER        | NOT NULL, DEFAULT 0, CHECK (≥ 0)                 | Number of physical copies currently in inventory |
| Price            | DECIMAL(10,2)  | NOT NULL, CHECK (≥ 0)                            | Current selling price |
| BPublisherID     | INTEGER        | NOT NULL, FOREIGN KEY → Publisher(PublisherID)   | Publisher that released this book |

**Foreign key behavior:**  
- `ON UPDATE CASCADE` – if a PublisherID changes, the book is updated automatically.  
- `ON DELETE RESTRICT` – a publisher cannot be deleted while books still reference it.

### 2.3 Author
**Real-world entity:** A person who writes books.

| Attribute  | Data Type     | Constraints                | Description |
|------------|---------------|----------------------------|-------------|
| AuthorID   | INTEGER       | PRIMARY KEY, AUTOINCREMENT | Unique identifier for the author |
| Bio        | TEXT          | —                          | Optional short biography |
| FirstName  | VARCHAR(30)   | NOT NULL                   | Author’s first name |
| MiddleName | VARCHAR(100)  | —                          | Author’s middle name or initials, when present |
| LastName   | VARCHAR(30)   | NOT NULL                   | Author’s last name |

### 2.4 Category
**Real-world entity:** A genre or subject classification used to organize books (e.g., Fantasy, Technical, Fiction).

| Attribute     | Data Type     | Constraints                | Description |
|---------------|---------------|----------------------------|-------------|
| CategoryID    | INTEGER       | PRIMARY KEY, AUTOINCREMENT | Unique identifier for the category |
| CategoryName  | VARCHAR(30)   | NOT NULL                   | Name of the category |
| Description   | TEXT          | —                          | Optional longer description of the category |

### 2.5 Customer
**Real-world entity:** A person who buys books from the store.

| Attribute   | Data Type     | Constraints                | Description |
|-------------|---------------|----------------------------|-------------|
| CustomerID  | INTEGER       | PRIMARY KEY, AUTOINCREMENT | Unique identifier for the customer |
| FirstName   | VARCHAR(30)   | NOT NULL                   | Customer’s first name |
| LastName    | VARCHAR(30)   | NOT NULL                   | Customer’s last name |
| Email       | VARCHAR(80)   | NOT NULL, UNIQUE           | Email address (must be unique) |
| Phone       | VARCHAR(20)   | —                          | Contact phone number |
| Street      | VARCHAR(80)   | —                          | Street address |
| City        | VARCHAR(50)   | —                          | City |
| State       | VARCHAR(30)   | —                          | State or province |
| ZIPCode     | VARCHAR(10)   | —                          | Postal / ZIP code |

### 2.6 Employee
**Real-world entity:** A staff member who works at the bookstore and may process orders.

| Attribute   | Data Type      | Constraints                                      | Description |
|-------------|----------------|--------------------------------------------------|-------------|
| EmployeeID  | INTEGER        | PRIMARY KEY, AUTOINCREMENT                       | Unique identifier for the employee |
| FirstName   | VARCHAR(30)    | NOT NULL                                         | Employee’s first name |
| LastName    | VARCHAR(30)    | NOT NULL                                         | Employee’s last name |
| Email       | VARCHAR(80)    | NOT NULL, UNIQUE                                 | Work email address |
| Phone       | VARCHAR(20)    | —                                                | Contact phone number |
| Position    | VARCHAR(50)    | —                                                | Job title (e.g., Cashier, Manager) |
| HourlyRate  | DECIMAL(8,2)   | CHECK (NULL or ≥ 0)                              | Pay rate per hour (optional) |

### 2.7 Orders
**Real-world entity:** A customer purchase transaction.

| Attribute      | Data Type     | Constraints                                                                 | Description |
|----------------|---------------|-----------------------------------------------------------------------------|-------------|
| OrderID        | INTEGER       | PRIMARY KEY, AUTOINCREMENT                                                  | Unique identifier for the order |
| OrderDate      | DATE          | NOT NULL                                                                    | Date the order was placed |
| PaymentMethod  | VARCHAR(30)   | NOT NULL, CHECK (IN ('Credit Card','Debit Card','Cash','Gift Card','PayPal')) | How the customer paid |
| OrderStatus    | VARCHAR(30)   | NOT NULL, CHECK (IN ('Pending','Processing','Shipped','Delivered','Cancelled')) | Current status of the order |
| OCustomerID    | INTEGER       | NOT NULL, FOREIGN KEY → Customer(CustomerID)                                | Customer who placed the order |
| OEmployeeID    | INTEGER       | FOREIGN KEY → Employee(EmployeeID)                                          | Employee who handled the order (optional) |

**Foreign key behavior:**  
- Customer: `ON DELETE RESTRICT` (cannot delete a customer who has orders).  
- Employee: `ON DELETE SET NULL` (if the employee is removed, the order keeps its history).

### 2.8 Order_Item
**Real-world entity:** A single line item inside an order (one book + quantity).

| Attribute    | Data Type      | Constraints                                      | Description |
|--------------|----------------|--------------------------------------------------|-------------|
| OrderItemID  | INTEGER        | PRIMARY KEY, AUTOINCREMENT                       | Unique identifier for the line item |
| Quantity     | INTEGER        | NOT NULL, CHECK (> 0)                            | Number of copies ordered |
| UnitPrice    | DECIMAL(10,2)  | NOT NULL, CHECK (≥ 0)                            | Price charged for one copy at the time of order |
| OOrderID     | INTEGER        | NOT NULL, FOREIGN KEY → Orders(OrderID)          | Parent order |
| OISBN        | VARCHAR(13)    | NOT NULL, FOREIGN KEY → Book(ISBN)               | Book that was ordered |

**Foreign key behavior:**  
- Deleting an Order automatically deletes its Order_Items (`ON DELETE CASCADE`).  
- A book cannot be deleted while it appears in any order (`ON DELETE RESTRICT`).

### 2.9 BookRating
**Real-world entity:** A customer’s star rating of a book.

| Attribute    | Data Type  | Constraints                                      | Description |
|--------------|------------|--------------------------------------------------|-------------|
| RatingID     | INTEGER    | PRIMARY KEY, AUTOINCREMENT                       | Unique identifier for the rating |
| Rating       | INTEGER    | NOT NULL, CHECK (BETWEEN 1 AND 5)                | Star rating (1–5) |
| RISBN        | VARCHAR(13)| NOT NULL, FOREIGN KEY → Book(ISBN)               | Book being rated |
| RCustomerID  | INTEGER    | NOT NULL, FOREIGN KEY → Customer(CustomerID)     | Customer who gave the rating |

The pair `(RCustomerID, RISBN)` is UNIQUE: each customer can rate each book once.

### 2.10 Writes (Junction Table)
**Real-world entity:** The many-to-many relationship between books and authors (a book can have multiple authors; an author can write many books).

| Attribute  | Data Type   | Constraints                                      | Description |
|------------|-------------|--------------------------------------------------|-------------|
| WISBN      | VARCHAR(13) | PRIMARY KEY (composite), FOREIGN KEY → Book      | Book ISBN |
| WAuthorID  | INTEGER     | PRIMARY KEY (composite), FOREIGN KEY → Author    | Author ID |

Both foreign keys use `ON DELETE CASCADE` so that removing a book or author cleans up the relationship automatically.

### 2.11 Is_In (Junction Table)
**Real-world entity:** The many-to-many relationship between books and categories.

| Attribute    | Data Type   | Constraints                                      | Description |
|--------------|-------------|--------------------------------------------------|-------------|
| IISBN        | VARCHAR(13) | PRIMARY KEY (composite), FOREIGN KEY → Book      | Book ISBN |
| ICategoryID  | INTEGER     | PRIMARY KEY (composite), FOREIGN KEY → Category  | Category ID |

---

## 3. Important Relationships

```
Publisher 1 ─── * Book
Author    * ─── * Book          (via Writes)
Category  * ─── * Book          (via Is_In)
Customer  1 ─── * Orders
Employee  1 ─── * Orders        (optional)
Orders    1 ─── * Order_Item
Book      1 ─── * Order_Item
Book      1 ─── * BookRating
Customer  1 ─── * BookRating
```

**Note on derived data:**  
The total price of an order is **not stored**. It is calculated when needed:

```sql
SELECT OOrderID, SUM(Quantity * UnitPrice) AS OrderPrice
FROM Order_Item
GROUP BY OOrderID;
```

---

## 4. Instructions for Adding Records

Always enable foreign-key enforcement before making changes:

```sql
PRAGMA foreign_keys = ON;
```

### 4.1 Adding a Publisher
```sql
INSERT INTO Publisher (Name)
VALUES ('HarperCollins');
```

### 4.2 Adding an Author
```sql
INSERT INTO Author (FirstName, LastName, Bio)
VALUES ('Terry', 'Pratchett', 'British author of the Discworld series.');
```

### 4.3 Adding a Book
```sql
INSERT INTO Book (ISBN, Title, PublicationYear, StockQuantity, Price, BPublisherID)
VALUES ('9780060853983', 'Going Postal', 2004, 12, 7.99, 1);
```

### 4.4 Linking an Author to a Book
```sql
INSERT INTO Writes (WISBN, WAuthorID)
VALUES ('9780060853983', 1);
```

### 4.5 Adding a Customer
```sql
INSERT INTO Customer (FirstName, LastName, Email, City, State)
VALUES ('Avery', 'Reader', 'avery.reader@example.com', 'Austin', 'TX');
```

### 4.6 Creating an Order and Order Items
```sql
-- 1. Create the order header
INSERT INTO Orders (OrderDate, PaymentMethod, OrderStatus, OCustomerID)
VALUES ('2026-10-15', 'Credit Card', 'Delivered', 1);

-- 2. Immediately capture the generated ID, e.g. SELECT last_insert_rowid();
-- 3. Use that saved order ID for every item (replace :order_id).
INSERT INTO Order_Item (Quantity, UnitPrice, OOrderID, OISBN)
VALUES (2, 7.99, :order_id, '9780060853983');
```

### 4.7 Adding a Rating
```sql
INSERT INTO BookRating (Rating, RISBN, RCustomerID)
VALUES (5, '9780060853983', 1);
```

---

## 5. Instructions for Removing Records

**Important warnings:**
- Foreign-key constraints will prevent deletion if dependent records exist.
- Use `ON DELETE CASCADE` relationships carefully — they will automatically remove related rows.
- Always back up the database before bulk deletes.

### 5.1 Safe deletion examples

```sql
-- Delete a rating (no other tables depend on it)
DELETE FROM BookRating WHERE RatingID = 5;

-- Delete an order (Order_Items are automatically removed because of CASCADE)
DELETE FROM Orders WHERE OrderID = 12;

-- Delete a book that has no order history or ratings
DELETE FROM Book WHERE ISBN = '9780000000000';
```

### 5.2 Deletions that will be blocked

```sql
-- This will FAIL if the book appears in any Order_Item or BookRating
DELETE FROM Book WHERE ISBN = '9780060853983';

-- This will FAIL if the customer has any orders
DELETE FROM Customer WHERE CustomerID = 1;
```

### 5.3 Recommended approach for complex deletions

1. First remove dependent records (Order_Items, BookRatings, Writes, Is_In).
2. Then delete the parent record.
3. Or use a transaction so you can roll back if something goes wrong:

```sql
BEGIN TRANSACTION;
-- delete dependent rows first
DELETE FROM Order_Item WHERE OISBN = '9780060853983';
DELETE FROM BookRating WHERE RISBN = '9780060853983';
DELETE FROM Writes WHERE WISBN = '9780060853983';
DELETE FROM Is_In WHERE IISBN = '9780060853983';
-- finally delete the book
DELETE FROM Book WHERE ISBN = '9780060853983';
COMMIT;
```

---

## 6. Quick Reference – Common Maintenance Tasks

| Task                        | Recommended Approach                                      |
|-----------------------------|-----------------------------------------------------------|
| Reduce stock after a sale   | `UPDATE Book SET StockQuantity = StockQuantity - ? WHERE ISBN = ?` |
| Change book price           | `UPDATE Book SET Price = ? WHERE ISBN = ?`                   |
| Cancel an order             | `UPDATE Orders SET OrderStatus = 'Cancelled' WHERE OrderID = ?` |
| Find low-stock books        | `SELECT Title, StockQuantity FROM Book WHERE StockQuantity < 5` |

---

**End of User Manual**
