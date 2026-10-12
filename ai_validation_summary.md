# AI Validation Summary: Bits & Books Relational Schema

**Tool used:** Claude (Anthropic)
**Input:** the Relational Schema document and the revised Chen-notation ERD
**Checks performed:** consistency with the ERD, representation of all relationships, key constraints

---

## 1. Consistency with the ERD

| Check | Result |
|---|---|
| All 9 entities (Employee, Customer, Order, Order_Item, Book, Publisher, Author, Category, BookRating) have a table | Pass |
| Attributes match the ERD | Pass, with one exception: OrderPrice (see feedback item 2) |
| Composite attributes (Customer Address, Author Name) flattened into atomic columns | Pass |
| Table and column names are consistent with the ERD | Pass |

## 2. Relationship coverage

| ERD relationship | Cardinality | Schema representation | Result |
|---|---|---|---|
| PROCESSES | Employee 0..N, Order 0..1 | Order.OEmployeeID references Employee | Pass |
| PLACES | Customer 0..N, Order 1..1 | Order.OCustomerID references Customer | Pass |
| CONTAINS | Order 1..N, Order_Item 1..1 | Order_Item.OOrderID references Order | Pass |
| GIVES | Customer 0..N, BookRating 1..1 | BookRating.RCustomerID references Customer | Pass |
| ABOUT | BookRating 1..1, Book 0..N | BookRating.RISBN references Book | Pass |
| PUBLISHED_BY | Book 1..1, Publisher 0..N | Book.BPublisherID references Publisher | Pass |
| WRITES | Many-to-many | Writes (WISBN, WAuthorID) | Pass |
| IS_IN | Many-to-many | Is_In (IISBN, ICategoryID) | Pass |
| Order_Item to Book | Not clearly drawn in the ERD | Order_Item.OISBN references Book | Pass in the schema, but the ERD needs a relationship drawn for it |

All relationships are represented. The two many-to-many relationships are correctly split into junction tables, and every one-to-many foreign key is on the "many" side.

## 3. Key constraint validation

- **Primary keys:** every table has one. Book uses the natural key ISBN, Writes and Is_In use composite keys, and the remaining tables use surrogate integer IDs.
- **Foreign keys:** every foreign key references an existing table and a primary key of matching data type.
- **Referential paths:** there are no orphan tables, and no foreign key points to the wrong table.

## 4. AI feedback and changes made

| # | Feedback | Change made |
|---|---|---|
| 1 | ISBN is typed INT, which cannot hold a 13-digit ISBN (the INT maximum is about 2.1 billion). ISBNs can also have leading zeros, and ISBN-10 can end in "X". | Changed ISBN to VARCHAR(13), and changed RISBN, OISBN, WISBN and IISBN to match. |
| 2 | OrderPrice is stored as a column, but the ERD shows it as a derived (dashed) attribute. | Removed OrderPrice from the Order table. It is computed as SUM(Quantity × UnitPrice) over the order's items. |
| 3 | The schema does not state which foreign keys are NOT NULL, so the ERD's participation constraints (1..1 vs 0..1) are not visible. | Marked BPublisherID, OCustomerID, OOrderID, RCustomerID, RISBN and OISBN as NOT NULL. OEmployeeID stays nullable (0..1). |
| 4 | BookID is an extra identifier in Book but has no uniqueness rule. | Declared BookID UNIQUE, as an alternate key. |
| 5 | Title is VARCHAR(30) and Publisher Name is VARCHAR(30), which will truncate many real values. | Increased Title to VARCHAR(200) and Publisher Name to VARCHAR(100). |
| 6 | The Order entry runs together with its Foreign Key lines. The notation "#" and "FK" is not defined, and the composite keys of Writes and Is_In are not stated. | Separated the lines, added a notation legend ("# = primary key, FK = foreign key"), and stated that Writes and Is_In have composite primary keys. |
| 7 | The assumptions contain a typo ("only once publisher") and do not cover minimum cardinalities (Order 1..N items, Book 1..N authors), the Rating range, or delete behavior. | Fixed the typo. Added assumptions on minimum cardinalities, Rating between 1 and 5, ON DELETE behavior, and UnitPrice storing the price at the time of sale. |
| 8 | The ERD does not clearly show how Order_Item connects to Book. | Documented the assumption that each order item refers to exactly one book. Recommended updating the ERD with a separate relationship (Order_Item 1..1, Book 0..N). |

The updated schema with all of these changes is in `Relational_Schema_Updated.md`.

## 5. Conclusion

The schema covers all entities and all eight ERD relationships, and its primary and foreign keys are valid. The main problems were the ISBN data type, the stored derived attribute (OrderPrice), unstated NOT NULL constraints, and thin documentation of assumptions. After the changes above, the schema is consistent with the ERD.
