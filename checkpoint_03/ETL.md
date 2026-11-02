# ETL notes

`etl.py` recreates the database locally from the supplied schema and source CSV.

1. It reads the CSV as Windows-1252 because the source includes characters outside UTF-8.
2. It skips the title/header rows and parses each book's ISBN, title, first author, publisher, year, price, and category.
3. Rows with a blank ISBN and a populated author cell are coauthors of the preceding book. The loader attaches those names to that book rather than treating them as separate records.
4. Publisher and category records are reused by name. Author records are reused by first and last name. It inserts the normalized catalog records and their `Writes` and `Is_In` relationships.
5. It adds a small sample set of customers, an employee, linked orders and order items, and one rating. The customer with email `email_example` gives the customer-specific queries a stable example. Foreign key checks are enabled.

The sample order and stock values are demonstration data because the source CSV only supplies catalog information. The supplied CSV remains unchanged in the package.
