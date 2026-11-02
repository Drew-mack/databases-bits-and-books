# Checkpoint 03: SQLite Implementation and Query Output

This package contains the SQLite database built from `schema.sql`, the supplied book catalog, related sample records, and captured results for queries (a)-(f).

Run `python3 etl.py` from this folder to recreate `bits_and_books.db` from the included CSV and schema. `queries.sql` contains the six executable queries; `query_output.md` records their results against the included database.

The source `queries.sql` in the project had a stray `SQLite format 3` line and a malformed ending on query (f). Those were removed/corrected in this package. Query (a) returns the supplied Terry Pratchett titles priced below $10.
