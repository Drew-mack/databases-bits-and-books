# Bits & Books — Checkpoint 1

## 1. Entity Identification

### Book catalog

- **Book:** BookID, Title, ISBN, PublicationDate, Price, StockQuantity
- **Author:** AuthorID, Name, Bio
- **Publisher:** PublisherID, Name
- **Category:** CategoryID, CategoryName, Description
- **BookAuthor:** BookID, AuthorID

### Customers and purchases

- **Customer:** CustomerID, FirstName, LastName, Email, Phone, Address
- **Order:** OrderID, OrderDate, OrderPrice, PaymentMethod, OrderStatus
- **Order_Item:** OrderItemID, Quantity, UnitPrice

### Additional Entities

- **BookRating:** Rating, CustomerID, BookID
- **Employee:** EmployeeID, FirstName, LastName, Email, Phone, Position, HourlyRate

## 2. Relationship Mapping

### Catalog relationships

- A Publisher publishes Books. One publisher can publish many books, and each book must have one publisher.
- A Category contains Books through the Is_In relationship. A category can contain many books, and a book can belong to multiple categories.
- A Book has BookAuthor entries. One book can have multiple BookAuthor entries, and each entry is associated with one book.
- A BookAuthor entry has one Author. An author can be connected to many BookAuthor entries, allowing an author to write multiple books and a book to have multiple authors.

### Sales and inventory relationships

- A Customer places Orders. One customer can place many orders, and each order belongs to one customer.
- An Employee processes Orders. One employee can process many orders, and each order is processed by one employee.
- An Order contains Order_Items. One order can contain many order items, and each order item belongs to one order.
- An Order_Item is selected as one Book. A book can appear in many order items, while each order item refers to one book.

### Additional relationships

- A Customer gives BookRatings. Each rating belongs to one customer, and a customer may give zero or many ratings.
- A BookRating is reviewed by one Book. A book may receive many ratings, while each rating describes one book.

## 3. Extended Design

### BookRating — customer ratings

**Attributes:** Rating, CustomerID, BookID.

**Relationships:** Each BookRating connects one Customer to one Book. Customers can rate multiple books, and books can receive ratings from multiple customers.

Ratings range from 1 to 5. A customer can have one rating per book and can update it later.

**Rationale:** Book ratings help customers compare books using feedback from other readers.

### Employee — order fulfillment

**Attributes:** EmployeeID, FirstName, LastName, Email, Phone, Position, HourlyRate.

**Relationships:** An Employee processes Orders in a one-to-many relationship. One employee can process many orders, and each order is processed by one employee.

**Rationale:** Employee records let the store maintain staff information and track which employee processes each customer order.

## 4. Informal Queries

1. Customer purchase history: Which books has a selected customer purchased, on what dates, and how much did each order cost?
2. Search books based on filters like selected author and publisher.
3. BookRating report: What is a selected book's average rating, and how many customers have rated it?
4. Employee assignment report: Which orders are assigned to a selected employee, including each order's date and the books and quantities to prepare?

## 5. Design Flexibility

Create a Publisher record with a new PublisherID and its name. No Book record is required because the publisher's relationship to books allows zero books. When a book is entered later, its PublisherID connects it to the existing publisher. Each book still has one publisher.

## 6. Update Operations

1. Record a purchase. Create a CustomerOrder and its OrderItems, recording the quantity and actual unit price paid for each book. Check that enough copies are available, then reduce Book.Quantity by the number purchased. Save these changes together.
2. Update customer information. Change a customer's Email, Phone, or Address when their contact information changes, keeping the same CustomerID.
3. Add or update a book rating (BookRating). Record the customer, book, and rating from 1 to 5 in BookRating. If the customer has already rated that book, update the existing rating.
4. Assign an employee to an order (Employee). When preparation begins, update CustomerOrder.EmployeeID with the employee responsible for fulfillment. If responsibility changes, replace the assignment with the new employee's ID.
