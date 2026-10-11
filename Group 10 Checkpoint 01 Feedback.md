# Group 10 Checkpoint 01 Feedback

## Summary

Your team's answers describe a sound starting design: all core entities are present, every relationship has a cardinality, and BOOKRATING and EMPLOYEE are well-scoped extensions. The biggest gap is the missing ERD, which this checkpoint requires. Next, replace BOOKAUTHOR with an M:N relationship, remove foreign keys from attribute lists, mark keys, and state participation for every relationship.

## What Is Working Well

- All core entities are present (BOOK, AUTHOR, PUBLISHER, CUSTOMER, ORDER), and `StockQuantity` on BOOK works for one online store.
- AUTHOR is its own entity, and a book can have several authors, as many books in the data file do.
- ORDER_ITEM, linked 1:N to ORDER and N:1 to BOOK, lets an order hold many books, keeps the price paid, and lists no foreign keys.
- Section 5 correctly allows a publisher with no books.
- BOOKRATING and EMPLOYEE are simple, useful extensions, each with attributes, a relationship, a rationale, a query, and an update.

## Top Priorities Before Checkpoint 02

1. **Submit `ERD/ERD.png`** in Chen notation with every entity and relationship, then run your AI check on it.
2. **Replace BOOKAUTHOR with one M:N WRITES relationship** between AUTHOR and BOOK.
3. **Remove foreign keys from attribute lists**, such as `CustomerID` and `BookID` on BOOKRATING. The relationships carry these links.
4. **Mark a key for every entity**, such as `ISBN` for BOOK and a new `RatingID` for BOOKRATING.
5. **State participation on both sides of every relationship**, and let an order have zero or one employee in PROCESSES.
6. **Make AUTHOR `Name` and CUSTOMER `Address` composite**, and use one name per entity and attribute.

## Detailed Feedback

### Entity Identification

- CATEGORY as an entity with an M:N link to BOOK is a good choice. The data file lists ISBN 0743206061 under two categories.
- BOOKAUTHOR only links a book to an author and has no attributes of its own, so in Chen notation it is an M:N relationship, WRITES. The linking table belongs in the Checkpoint 02 schema.
- ORDER_ITEM has its own attributes, so it can stay an entity. If `OrderItemID` is only a line number within an order, make it a weak entity owned by ORDER.

### Attributes and Keys

- No key is marked, so it is unclear what identifies each entity. Underline a key in each regular entity; a weak entity gets a dashed-underlined partial key.
- BOOK lists both `BookID` and `ISBN`. Since every book in the data has an ISBN, make `ISBN` the key and drop `BookID`.
- Make AUTHOR `Name` (`FirstName`, `MiddleName`, `LastName`) and CUSTOMER `Address` (`Street`, `City`, `State`, `Zip`) composite. The data has author names such as "Ian H. Witten".
- PUBLISHER has only `PublisherID` and `Name`. Add contact details such as `Phone` or `Email`.
- Without its foreign keys, BOOKRATING has only `Rating`, which is not unique. Add a `RatingID` key and consider `RatingDate`. Your rule of one rating per customer per book becomes a unique constraint in Checkpoint 02.
- `OrderPrice` can be calculated from the order items, and `UnitPrice` already keeps the price paid, so past totals stay correct. Draw `OrderPrice` as a derived attribute (dashed oval), unless it also holds tax or shipping.
- The data gives only a year, so `PublicationYear` fits better than `PublicationDate`.
- Keep `PublisherID` (Section 5) and `EmployeeID` (update 4) off the ERD, because PUBLISHES and PROCESSES carry those links.

### Relationship Modeling

- In your answers, every entity is in at least one relationship, with no ternary relationships or redundant paths.
- Rename "is selected as" (ORDER_ITEM to BOOK) to REFERS_TO, which matches your own phrase "refers to one book".
- "A BookRating is reviewed by one Book" reads backward. Use RATES (BOOKRATING rates BOOK).
- Section 2 says a category "contains" books "through the Is_In relationship", but CONTAINS already links ORDER and ORDER_ITEM. Write BOOK IS_IN CATEGORY so the diagram and text agree.

### Cardinality and Participation

Based on your answers, put each label on the line joining the diamond to the entity named. Draw a double line (total participation) from the entities in the last column and a single line (partial) from the rest.

| Relationship | Labels | Double line from |
|---|---|---|
| PUBLISHES | 1 PUBLISHER, N BOOK | BOOK |
| WRITES (replaces BOOKAUTHOR) | M AUTHOR, N BOOK | BOOK; AUTHOR is your choice |
| IS_IN | M BOOK, N CATEGORY | BOOK (every book in the data has a category) |
| PLACES | 1 CUSTOMER, N ORDER | ORDER |
| PROCESSES | 1 EMPLOYEE, N ORDER | Neither |
| CONTAINS | 1 ORDER, N ORDER_ITEM | Both |
| REFERS_TO (now "is selected as") | N ORDER_ITEM, 1 BOOK | ORDER_ITEM |
| GIVES | 1 CUSTOMER, N BOOKRATING | BOOKRATING |
| RATES (now "is reviewed by") | N BOOKRATING, 1 BOOK | BOOKRATING |

- Your answers say which side needs exactly one, such as "each order belongs to one customer." Most do not say whether the other side can have none, and IS_IN states neither side. State both sides; for example, a customer may have no orders, but an order needs at least one item.

### ERD Clarity and Notation

- The `ERD/` folder is empty, so there is no diagram to review.
- Use Chen notation (not crow's foot or UML) in a tool with Chen shapes, such as draw.io or lucid.app. Show:
  - entities as rectangles and relationships as diamonds, linked entity to diamond to entity, never entity to entity;
  - attributes as ovals, with keys underlined, composite parts as smaller ovals, and derived attributes dashed;
  - a clearly placed 1, M, or N label on every line, and double or single lines for participation.
- Keep text readable, attributes beside their entity, and line crossings few.

### Completeness and Alignment with Requirements

- Sections 1 to 6 are all present, with the required queries and updates.
- Query 2 ("filters like selected author and publisher") is vague. Name its exact inputs and outputs.
- Both Markdown files are named correctly; only `ERD/ERD.png` is missing.
- Add headings and bullets to the AI summary; its five feedback items now display as one paragraph.

### Consistency Between Answers and ERD

- Once you draw the ERD, make it match your final answers.
- Pick one name for each of these:
  - "Order" (Section 1) and "CustomerOrder" (updates 1 and 4). "CustomerOrder" is safer, since ORDER is a reserved word in SQL.
  - "Order_Item" (Section 1) and "OrderItems" (update 1).
  - `StockQuantity` (Section 1) and `Book.Quantity` (update 1).
  - "Order_Item" and "Is_In" use underscores; "BookAuthor" and "BookRating" do not.
- The AI summary says the order-employee relationship was made "not a must", but Sections 2 and 3 still say "each order is processed by one employee." Change both to "zero or one employee", which matches update 4.

### AI Validation and Prompting

- The AI raised good questions about the order total and employee assignment, and you acted on the employee rule.
- Add your exact prompts, and say whether the AI saw an ERD image, a text listing, or both.
- The summary does not report the three required checks: disconnected entities, missing relationships, and naming consistency. Ask for each directly, as in the prompt below.
- For the BOOKAUTHOR, BOOKRATING key, and uniqueness suggestions, say whether you accepted or rejected each one, and why. Underlining `ISBN` as BOOK's key settles the ISBN part.
- Renaming `TotalAmount` to `OrderPrice` does not answer the AI's point that the total can be calculated (see Attributes and Keys).
- The reported AI feedback uses table terms (rows and IDs), keeps BOOKAUTHOR as an entity, and does not flag the foreign keys in your attribute lists or the single AUTHOR `Name`. Check its advice against Chen rules.
- Once `ERD/ERD.png` exists, rerun the check on the image and report the results and your changes.

A stronger prompt for your design:

> Review the attached Chen-notation ERD for an online bookstore. Below are the checkpoint instructions and Sections 1 to 3 and 5 of the answers. Intended design: AUTHOR WRITES BOOK (M:N; book total, author [total or partial]); PUBLISHER PUBLISHES BOOK (1:N; book total, publisher partial); BOOK IS_IN CATEGORY (M:N; book total, category partial); CUSTOMER PLACES ORDER (1:N; order total, customer partial); EMPLOYEE PROCESSES ORDER (1:N; both partial); ORDER CONTAINS ORDER_ITEM (1:N; both total); ORDER_ITEM REFERS_TO BOOK (N:1; order item total, book partial); CUSTOMER GIVES BOOKRATING (1:N; rating total, customer partial); BOOKRATING RATES BOOK (N:1; rating total, book partial). List: (1) entities with no relationship, or lines drawn entity to entity; (2) cardinality and participation as drawn, and mismatches with this list; (3) foreign keys drawn as attributes; (4) entities with no key marked; (5) composite or derived attributes drawn incorrectly; (6) inconsistent names or naming styles. Rank problems from most to least serious, with a fix for each. Answer in Chen ER terms, not tables or SQL.
