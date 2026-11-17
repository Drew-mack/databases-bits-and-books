# ETL and dataset notes

`source_catalog.csv` is the supplied Windows-1252 catalog. The importer trims fields, preserves ISBN as text, removes the `$` from prices, and stores the source publication year without inventing a date. A blank ISBN continues the previous book's author list. Each author cell is split on commas; words between the first and last name are stored as MiddleName. Repeated ISBNs reuse the Book row but still insert author/category relationships. Authors, categories and publishers are reused by name.

The built database contains 108 books, 101 authors, 141 book-author links, 61 publishers, 9 categories and 109 book-category links. It includes both Simon Benninga and Benjamin Czaczkes for ISBN 0262024829 and both categories for ISBN 0743206061. Twenty-eight author records have a middle name or initial.

The source does not provide customers, employees, orders, ratings, or stock. Those values are invented solely for demonstration: 4 customers, 1 employee, 4 orders, 7 order items and 2 ratings. Samples include an order with multiple line items, a zero-stock book, a customer without orders and two customers tied at five copies. Stock values are illustrative current stock, not a simulated inventory history.

To build from the CSV, run `python3 etl.py /path/to/new.sqlite`. The script refuses to overwrite an existing file. To rebuild from submission SQL instead, create a new SQLite database and run `schema.sql`, followed by `data.sql`; enable foreign keys for each connection. `generate_results.py` regenerates `query_results.md` and `data.sql` from `database.sqlite` and overwrites those two generated files.
