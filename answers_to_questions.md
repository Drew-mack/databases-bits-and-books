# Bits & Books — Checkpoint 1

## 1. Entity Identification

### Book catalog

- **Book:** BookID, ISBN, Name, Year, Price, Quantity, PublisherID
- **Author:** AuthorID, FirstName, MiddleName, LastName, Bio
- **Publisher:** PublisherID, Name
- **Category:** CategoryID, Name
- **BookAuthor:** BookID, AuthorID
- **BookCategory:** BookID, CategoryID

### Customers and purchases

- **Customer:** CustomerID, FirstName, LastName, Email, Password, Address, Phone
- **CustomerOrder:** CustomerOrderID, CustomerID, OrderDate, EmployeeID
- **OrderItem:** OrderItemID, CustomerOrderID, BookID, Quantity, UnitPrice

### Supplier orders

- **Supplier:** SupplierID, Name, Email, Phone, Address
- **StoreOrder:** StoreOrderID, SupplierID, OrderDate
- **StoreOrderItem:** StoreOrderItemID, StoreOrderID, BookID, Quantity, UnitCost

### Additional Entities

- **BookRating:** BookRatingID, Rating, CustomerID, BookID
- **Employee:** EmployeeID, FirstName, LastName, Email, Position

## 2. Relationship Mapping

### Catalog relationships

- A Publisher publishes Books. Each book has one publisher, while a publisher may have zero or many books recorded.
- An Author writes Books, connected through BookAuthor. Authors and books have a many-to-many relationship; each BookAuthor entry identifies one author and one book. Either can be entered before their authorship links are recorded.
- A Book belongs to Categories, connected through BookCategory. A book may have zero or many categories, and a category may have zero or many books. Each BookCategory entry connects one of each.

### Sales and inventory relationships

- A Customer places CustomerOrders. Each order belongs to one customer, and a customer may have zero or many orders.
- A CustomerOrder contains OrderItems. Each order has one or more items, and each item belongs to one order.
- An OrderItem references a Book. Each item identifies one book, and a book may appear in zero or many order items.
- A Supplier receives StoreOrders. Each store order goes to one supplier, and a supplier may have zero or many store orders.
- A StoreOrder contains StoreOrderItems. Each store order has one or more items, and each item belongs to one store order.
- A StoreOrderItem references a Book. Each item identifies one book, and a book may appear in zero or many store order items.

### Additional relationships

- A Customer gives BookRatings. Each rating belongs to one customer, and a customer may give zero or many ratings.
- A Book receives BookRatings. Each rating describes one book, and a book may receive zero or many ratings.
- An Employee fulfills CustomerOrders. An employee may be assigned zero or many orders. Each order may have no employee assigned yet or one employee responsible for fulfillment.

## 3. Extended Design

### BookRating — customer ratings

**Attributes:** BookRatingID, Rating, CustomerID, BookID.

**Relationships:** Each BookRating connects one Customer to one Book. Customers can rate multiple books, and books can receive ratings from multiple customers.

Ratings range from 1 to 5. A customer can have one rating per book and can update it later.

**Rationale:** Book ratings help customers compare books using feedback from other readers.

### Employee — order fulfillment

**Attributes:** EmployeeID, FirstName, LastName, Email, Position.

**Relationships:** An Employee may fulfill many CustomerOrders. Each order can have one assigned employee or remain unassigned until fulfillment begins, using EmployeeID in CustomerOrder to record the assignment.

**Rationale:** Employee records let the store track which staff member is responsible for preparing each online order.

## 4. Informal Queries

1. Customer purchase history: Which books has a selected customer purchased, on what dates, and how much did each order cost?
2. Supplier purchasing report: For a selected month, which books did the store order from each supplier, in what quantities, and at what total cost?
3. BookRating report: What is a selected book's average rating, and how many customers have rated it?
4. Employee assignment report: Which orders are assigned to a selected employee, including each order's date and the books and quantities to prepare?

## 5. Design Flexibility

Create a Publisher record with a new PublisherID and its name. No Book record is required because the publisher's relationship to books allows zero books. When a book is entered later, its PublisherID connects it to the existing publisher. Each book still has one publisher.

## 6. Update Operations

1. Record a purchase. Create a CustomerOrder and its OrderItems, recording the quantity and actual unit price paid for each book. Check that enough copies are available, then reduce Book.Quantity by the number purchased. Save these changes together.
2. Update customer information. Change a customer's Email, Phone, or Address when their contact information changes, keeping the same CustomerID.
3. Place a supplier order. Create a StoreOrder for the selected supplier and add StoreOrderItems for the books being ordered, recording each book's quantity and unit cost.
4. Add or update a book rating (BookRating). Record the customer, book, and rating from 1 to 5 in BookRating. If the customer has already rated that book, update the existing rating.
5. Assign an employee to an order (Employee). When preparation begins, update CustomerOrder.EmployeeID with the employee responsible for fulfillment. If responsibility changes, replace the assignment with the new employee's ID.

## 7. ERD Diagram

The diagram will be created manually and saved as ERD/ERD.png. It will include all 14 entities, their attributes, and the relationships above. BookRating connects to Customer and Book, and Employee connects to CustomerOrder.
