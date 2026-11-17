# AI query validation summary

**AI tool:** OpenAI Codex  
**Validation scope:** Queries (a)–(n) in `queries.sql`, run against the submitted `database.sqlite` and compared with `query_results.md` and the Checkpoint 04 questions.

All 14 queries executed successfully. Their results matched independent calculations from the database, and the saved `query_results.md` matched a fresh execution. The checks below apply to the submitted sample data.

| Query | Feedback | Rows |
|---|---|---:|
| (a) | Returned the five Terry Pratchett titles priced below $10. | 5 |
| (b) | Returned Avery Reader's purchased titles and dates. | 3 |
| (c) | Returned books with stock below five, including the zero-stock example. | 3 |
| (d) | Returned the customers and Pratchett titles they purchased. | 4 |
| (e) | Avery Reader purchased five copies, summing item quantities. | 1 |
| (f) | Avery Reader and Casey Morgan tied for the most, at five copies each; both appeared. | 2 |
| (g) | Returned each customer's spending, including $0 for the customer with no orders. | 4 |
| (h) | Returned Casey and Avery, whose spending exceeds the $54.68 average across all four customers. | 2 |
| (i) | Returned book copy totals in descending order, including unsold books. | 108 |
| (j) | Returned book sales revenue in descending order, including unsold books. | 108 |
| (k) | Returned Terry Pratchett as the author with the most copies sold: eight. | 1 |
| (l) | Returned Stephen Wolfram as the highest-revenue author: $89.90. | 1 |
| (m) | Returned Casey Morgan, who purchased a book by the highest-revenue author. | 1 |
| (n) | Returned the four authors of books purchased by the high-spending customers from (h). | 4 |

A separate in-memory test verified that (f), (k), and (l) retain ties, and that (m) and (n) return the expected customers and authors in that test. Spending averages include customers with no purchases; all recorded orders count as purchases; and each coauthor receives full credit for a book's sales. For (i) and (j), unsold books are included with zero totals. The source CSV supplies the catalog; customer, order, employee, rating, and stock data are examples.

**Changes made after this validation:** None to the database, queries, or query results. The checks found no query changes necessary for the tested data and tie cases.
