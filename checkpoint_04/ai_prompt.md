# AI Prompt Used to Generate the User Manual

**Tool used:** Grok (xAI)

**Date:** November 15, 2026

---

## Primary Prompt

```
You are a technical writer creating a professional user manual for a bookstore database system called "Bits & Books".

Generate a clear, well-structured user manual based on the following SQLite schema. The manual must include:

1. An introduction explaining the purpose of the database.
2. For every table:
   - A real-world description (what business entity it represents)
   - A complete list of every attribute with:
     - Data type
     - Constraints (PRIMARY KEY, FOREIGN KEY, NOT NULL, UNIQUE, CHECK, DEFAULT, etc.)
     - A short plain-English explanation of what the attribute stores
3. Clear instructions for:
   - Adding new records (with example INSERT statements)
   - Removing records (with example DELETE statements and important warnings about foreign key constraints)
4. A short section on important relationships between tables.
5. A note about derived data (OrderPrice is calculated, not stored).

Use professional but accessible language suitable for a developer or database administrator. Format the manual in clean Markdown.

Here is the complete schema:

PRAGMA foreign_keys = ON;

CREATE TABLE Publisher (
    PublisherID INTEGER PRIMARY KEY AUTOINCREMENT,
    Name VARCHAR(100) NOT NULL
);

CREATE TABLE Book (
    ISBN VARCHAR(13) PRIMARY KEY,
    BookID INTEGER UNIQUE,
    Title VARCHAR(200) NOT NULL,
    PublicationDate DATE,
    StockQuantity INTEGER NOT NULL DEFAULT 0 CHECK (StockQuantity >= 0),
    Price DECIMAL(10,2) NOT NULL CHECK (Price >= 0),
    BPublisherID INTEGER NOT NULL,
    FOREIGN KEY (BPublisherID) REFERENCES Publisher(PublisherID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE Author (
    AuthorID INTEGER PRIMARY KEY AUTOINCREMENT,
    Bio TEXT,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL
);

CREATE TABLE Category (
    CategoryID INTEGER PRIMARY KEY AUTOINCREMENT,
    CategoryName VARCHAR(30) NOT NULL,
    Description TEXT
);

CREATE TABLE Customer (
    CustomerID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Email VARCHAR(80) NOT NULL UNIQUE,
    Phone VARCHAR(20),
    Street VARCHAR(80),
    City VARCHAR(50),
    State VARCHAR(30),
    ZIPCode VARCHAR(10)
);

CREATE TABLE Employee (
    EmployeeID INTEGER PRIMARY KEY AUTOINCREMENT,
    FirstName VARCHAR(30) NOT NULL,
    LastName VARCHAR(30) NOT NULL,
    Email VARCHAR(80) NOT NULL UNIQUE,
    Phone VARCHAR(20),
    Position VARCHAR(50),
    HourlyRate DECIMAL(8,2) CHECK (HourlyRate IS NULL OR HourlyRate >= 0)
);

CREATE TABLE Orders (
    OrderID INTEGER PRIMARY KEY AUTOINCREMENT,
    OrderDate DATE NOT NULL,
    PaymentMethod VARCHAR(30) NOT NULL
        CHECK (PaymentMethod IN ('Credit Card', 'Debit Card', 'Cash', 'Gift Card', 'PayPal')),
    OrderStatus VARCHAR(30) NOT NULL
        CHECK (OrderStatus IN ('Pending', 'Processing', 'Shipped', 'Delivered', 'Cancelled')),
    OCustomerID INTEGER NOT NULL,
    OEmployeeID INTEGER,
    FOREIGN KEY (OCustomerID) REFERENCES Customer(CustomerID)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (OEmployeeID) REFERENCES Employee(EmployeeID)
        ON UPDATE CASCADE ON DELETE SET NULL
);

CREATE TABLE Order_Item (
    OrderItemID INTEGER PRIMARY KEY AUTOINCREMENT,
    Quantity INTEGER NOT NULL CHECK (Quantity > 0),
    UnitPrice DECIMAL(10,2) NOT NULL CHECK (UnitPrice >= 0),
    OOrderID INTEGER NOT NULL,
    OISBN VARCHAR(13) NOT NULL,
    FOREIGN KEY (OOrderID) REFERENCES Orders(OrderID)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (OISBN) REFERENCES Book(ISBN)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE BookRating (
    RatingID INTEGER PRIMARY KEY AUTOINCREMENT,
    Rating INTEGER NOT NULL CHECK (Rating BETWEEN 1 AND 5),
    RISBN VARCHAR(13) NOT NULL,
    RCustomerID INTEGER NOT NULL,
    FOREIGN KEY (RISBN) REFERENCES Book(ISBN)
        ON UPDATE CASCADE ON DELETE RESTRICT,
    FOREIGN KEY (RCustomerID) REFERENCES Customer(CustomerID)
        ON UPDATE CASCADE ON DELETE RESTRICT
);

CREATE TABLE Writes (
    WISBN VARCHAR(13) NOT NULL,
    WAuthorID INTEGER NOT NULL,
    PRIMARY KEY (WISBN, WAuthorID),
    FOREIGN KEY (WISBN) REFERENCES Book(ISBN)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (WAuthorID) REFERENCES Author(AuthorID)
        ON UPDATE CASCADE ON DELETE CASCADE
);

CREATE TABLE Is_In (
    IISBN VARCHAR(13) NOT NULL,
    ICategoryID INTEGER NOT NULL,
    PRIMARY KEY (IISBN, ICategoryID),
    FOREIGN KEY (IISBN) REFERENCES Book(ISBN)
        ON UPDATE CASCADE ON DELETE CASCADE,
    FOREIGN KEY (ICategoryID) REFERENCES Category(CategoryID)
        ON UPDATE CASCADE ON DELETE CASCADE
);
```

---

## Follow-up Prompt (used for minor polishing)

```
Please refine the user manual you just generated. Make sure:
- Every table has a clear real-world mapping
- Attribute explanations are concise but complete
- Adding and removing instructions include important foreign-key warnings
- The tone remains professional and suitable for a final project submission
```

