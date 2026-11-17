# Checkpoint 04 working folder

This folder is the current working version. The eight files required for the ZIP are `database.sqlite`, `schema.sql`, `data.sql`, `queries.sql`, `query_results.md`, `ai_validation_summary.md`, `user_manual.md`, and `ai_prompt.md`. Other files in this folder support rebuilding, validation and design review; they are not included in the submission ZIP.

- `database.sqlite`: populated SQLite database.
- `schema.sql`: tables, keys and constraints.
- `data.sql`: INSERT statements to populate a fresh schema.
- `queries.sql`: all fourteen checkpoint queries.
- `query_results.md`: output of those queries against the supplied database.
- `ai_validation_summary.md`: findings, changes, checks, assumptions and limits.
- `user_manual.md`: database tables, fields, relationships and maintenance examples.
- `ai_prompt.md`: manual-generation prompts and actual Codex task requests.
- `source_catalog.csv`: original catalog, kept in Windows-1252 encoding.
- `etl.py`: creates a new database from the source CSV and demonstration records; refuses to overwrite an existing file.
- `ETL.md`: import and sample-data explanation and counts.
- `generate_results.py`: regenerates query results and the SQL data export, overwriting those outputs.
- `validate.py`: CSV relationship, query, tie and constraint checks; runs read-only against the provided database and uses a separate in-memory test database.
- `relational_schema.md`: readable mapping of the final tables, keys and design choices.
- `ERD_Checkpoint04.drawio`: revised editable ERD source. Open in diagrams.net and visually review the layout before reusing or submitting it; no current image export has been verified.

Run `python3 validate.py`. For a new database use `python3 etl.py /path/to/new.sqlite`, or run `schema.sql` and then `data.sql` in a fresh SQLite database. Enable foreign keys on every connection. Sales, customers, employees, ratings and stock are demonstration data, and query assumptions are described in `queries.sql` and the validation summary.
