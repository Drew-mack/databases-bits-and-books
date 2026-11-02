# Captured query output

Executed against the included `bits_and_books.db` after running `etl.py`. Each result below is the output of its corresponding query.

## Query (a)

5 row(s).

| Title | Price |
| --- | --- |
| Going Postal | 7.99 |
| Guards! Guards! | 7.99 |
| Pyramids | 7.99 |
| Small Gods | 7.99 |
| Unseen Academicals | 7.99 |

## Query (b)

2 row(s).

| Title | PurchaseDate |
| --- | --- |
| Going Postal | 2026-10-01 |
| Guards! Guards! | 2026-10-15 |

## Query (c)

3 row(s).

| Title | ISBN | StockQuantity |
| --- | --- | --- |
| OCP: Oracle9i Certification Kit | 0782140661 | 2 |
| SQL Server 2000 for Experienced DBA's | 0072227885 | 2 |
| The Data Warehouse Toolkit: The Complete Guide to Dimensional Modeling | 0471200247 | 2 |

## Query (d)

3 row(s).

| FirstName | LastName | Title |
| --- | --- | --- |
| Avery | Reader | Going Postal |
| Avery | Reader | Guards! Guards! |
| Blair | Reader | Pyramids |

## Query (e)

1 row(s).

| FirstName | LastName | TotalBooks |
| --- | --- | --- |
| Avery | Reader | 3 |

## Query (f)

3 row(s).

| FirstName | LastName | TotalBooks |
| --- | --- | --- |
| Avery | Reader | 3 |
| Casey | Reader | 3 |
| Blair | Reader | 1 |

## Execution note

Query (f) ends in `ORDER BY TotalBooks DESC;` in this runnable copy; the project source had the invalid trailing text `total 928`. The stray leading text `SQLite format 3` was removed from the runnable SQL copy.
