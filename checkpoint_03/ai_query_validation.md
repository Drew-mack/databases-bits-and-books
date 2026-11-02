# AI query validation summary

**Tool:** OpenAI Codex

**Scope:** Reviewed queries (a)-(f), executed them against the included SQLite database, and compared the returned rows with each query's filters, joins, grouping, and sort order.

| Query | Validation | Result |
|---|---|---|
| (a) | Filters Terry Pratchett books to prices below $10 and sorts titles alphabetically. | Pass: five matching titles. |
| (b) | Selects the sample customer by email and returns purchased titles in purchase-date/title order. | Pass: two purchased titles across two dates. |
| (c) | Selects books with stock below five and sorts by stock then title. | Pass: three low-stock sample books. |
| (d) | Joins purchases to authors and returns distinct customers/titles for Terry Pratchett. | Pass: three customer/title rows. |
| (e) | Sums item quantities for the selected customer. | Pass: Avery Reader purchased three books. |
| (f) | Sums item quantities per customer and sorts totals descending. | Pass: three customers with totals 3, 3, and 1. |

**Feedback and changes:** The supplied query file began with the non-SQL text `SQLite format 3`, and query (f) ended with invalid trailing text `total 928`. These prevented direct execution. The runnable `queries.sql` copy removes the leading text and ends query (f) with `ORDER BY TotalBooks DESC;`. All six queries then executed successfully. The source catalog contains six Terry Pratchett titles; only five meet query (a)'s under-$10 condition. The sample email and purchase records are documented in `ETL.md` because the CSV does not contain customers or orders.

**Validation boundary:** These results confirm the queries against this package's included sample database. Customer, order, employee, rating, and stock values are demonstration data, not source-provided business records.
