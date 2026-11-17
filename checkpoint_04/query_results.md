# Checkpoint 04 query results

Generated from database.sqlite and queries.sql. Sample email for (b) and (e): avery.reader@example.com.

## (a) Titles of Terry Pratchett books priced below $10.

| Title |
| --- |
| Going Postal |
| Guards! Guards! |
| Pyramids |
| Small Gods |
| Unseen Academicals |

5 row(s).

## (b) Titles and purchase dates for Avery Reader.

| Title | OrderDate |
| --- | --- |
| A Field Guide to American Houses | 2026-10-01 |
| Going Postal | 2026-10-01 |
| Guards! Guards! | 2026-10-15 |

3 row(s).

## (c) Titles and ISBNs with fewer than five copies.

| Title | ISBN |
| --- | --- |
| A Field Guide to American Houses | 0394739698 |
| Going Postal | 0060502935 |
| Guards! Guards! | 0061020648 |

3 row(s).

## (d) Customers and titles for purchases of Terry Pratchett books.

| CustomerID | FirstName | LastName | Title |
| --- | --- | --- | --- |
| 1 | Avery | Reader | Going Postal |
| 1 | Avery | Reader | Guards! Guards! |
| 2 | Casey | Morgan | Pyramids |
| 3 | Blair | Reed | Going Postal |

4 row(s).

## (e) Copies purchased by Avery Reader, including zero if no purchases.

| CustomerID | FirstName | LastName | TotalBooks |
| --- | --- | --- | --- |
| 1 | Avery | Reader | 5 |

1 row(s).

## (f) All customers tied for the most copies purchased.

| CustomerID | FirstName | LastName | TotalBooks |
| --- | --- | --- | --- |
| 1 | Avery | Reader | 5 |
| 2 | Casey | Morgan | 5 |

2 row(s).

## (g) Total spending by every customer, including those with no orders.

| CustomerID | FirstName | LastName | TotalSpent |
| --- | --- | --- | --- |
| 1 | Avery | Reader | 56.91 |
| 2 | Casey | Morgan | 113.87 |
| 3 | Blair | Reed | 47.94 |
| 4 | Dana | Lee | 0.0 |

4 row(s).

## (h) Customers spending more than the average across all customers.

| CustomerID | FirstName | LastName | TotalSpent |
| --- | --- | --- | --- |
| 2 | Casey | Morgan | 113.87 |
| 1 | Avery | Reader | 56.91 |

2 row(s).

## (i) Titles and copies sold, including unsold books.

| ISBN | Title | CopiesSold |
| --- | --- | --- |
| 0060502935 | Going Postal | 3 |
| 0061020656 | Pyramids | 3 |
| 1579550088 | A New Kind of Science | 2 |
| 0061020648 | Guards! Guards! | 2 |
| 0394739698 | A Field Guide to American Houses | 1 |
| 0471288217 | A Visual Dictionary of Architecture | 1 |
| 0446608955 | A Walk to Remember | 0 |
| 0072222743 | A+ Certification All-in-One Exam Guide | 0 |
| 0782140114 | Access 2002 Developer's Handbook Set | 0 |
| 0324107501 | Advanced Accounting | 0 |
| 0385494246 | Amsterdam | 0 |
| 0072315318 | Analysis for Financial Management | 0 |
| 0471286168 | Architecture: Form, Space, and Order | 0 |
| 038572179X | Atonement | 0 |
| 0060934417 | Bel Canto: A Novel | 0 |
| 0471391123 | Beyond Coso : Internal Control to Enhance Corporate Governance | 0 |
| 0399149848 | Birthright | 0 |
| 0385494327 | Black Dogs | 0 |
| 0345336895 | Broca's Brain: Reflections on the Romance of Science | 0 |
| 0471358983 | Building Construction Illustrated | 0 |
| 1561586196 | Building a Shed | 0 |
| 1586851357 | Cabins & Camps | 0 |
| 0425188361 | Cerulean Sins | 0 |
| 0399149392 | Chesapeake Blue | 0 |
| 1579902944 | Choosing & Using Hand Tools | 0 |
| 0321125169 | ColdFusion MX Web Application Construction Kit | 0 |
| 0517576600 | Color: Natural Palettes for Painted Rooms | 0 |
| 0865659982 | Composers' Houses | 0 |
| 067976867X | Consilience: The Unity of Knowledge | 0 |
| 0671004107 | Contact | 0 |
| 0743244249 | Cosmopolis: A Novel | 0 |
| 0375508325 | Cosmos | 0 |
| 0972263608 | Creating Documents with BusinessObjects 5.1 | 0 |
| 1558605525 | Data Mining: Practical Machine Learning Tools and Techniques with Java Implementations | 0 |
| 0743467523 | Dreamcatcher | 0 |
| 0262232197 | Econometric Analysis of Cross Section and Panel Data | 0 |
| 0385494149 | Enduring Love | 0 |
| 0373218192 | Engaging The Enemy | 0 |
| 0743457358 | Everything's Eventual: 14 Dark Tales | 0 |
| 0609610570 | Execution: The Discipline of Getting Things Done | 0 |
| 0072294337 | Financial Markets & Corporate Strategy | 0 |
| 0262024829 | Financial Modeling | 0 |
| 0130323519 | Financial Reporting and Analysis | 0 |
| 0805317554 | Fundamentals of Database Systems | 0 |
| 0596004478 | Google Hacks | 0 |
| 0375703764 | House of Leaves | 0 |
| 0072227710 | How To Do Everything with Your Tablet PC | 0 |
| 0393318486 | How the Mind Works | 0 |
| 0471363049 | Intermediate Accounting | 0 |
| 0324113641 | Introductory Econometrics: A Modern Approach | 0 |
| 0071414339 | Investing in Fixer-Uppers : A Complete Guide to Buying Low, Fixing Smart, Adding Value, and Selling (or Renting) High | 0 |
| 0312276702 | Jinn: A Novel | 0 |
| 1565924916 | Ldap System Administration | 0 |
| 0373272839 | Letters to Kelly | 0 |
| 0738206679 | Linked: The New Science of Networks | 0 |
| 0373218257 | Love By Design | 0 |
| 0316096199 | Lucky: A Memoir | 0 |
| 0385504470 | Lullaby: A Novel | 0 |
| 0735713170 | Mac OS X v. 10.2 Jaguar Killer Tips | 0 |
| 0446606812 | Message in a Bottle | 0 |
| 0735712123 | MySQL | 0 |
| 0262521415 | Numerical Techniques in Finance | 0 |
| 0782140661 | OCP: Oracle9i Certification Kit | 0 |
| 0684843285 | ON FOOD AND COOKING | 0 |
| 067463442X | On Human Nature | 0 |
| 0743455967 | On Writing | 0 |
| 0345376595 | Pale Blue Dot: A Vision of the Human Future in Space | 0 |
| 0060540753 | Patron Saint of Liars | 0 |
| 1558606432 | Persuasive Technology: Using Computers to Change What We Think and Do | 0 |
| 0735712379 | Photoshop 7 Down & Dirty Tricks | 0 |
| 1586851322 | Prefab | 0 |
| 1861004486 | Professional SQL Server 2000 Programming | 0 |
| 0130998516 | Real World FPGA Design with Verilog | 0 |
| 0072227885 | SQL Server 2000 for Experienced DBA's | 0 |
| 0061092177 | Small Gods | 0 |
| 0670031518 | The Blank Slate: The Modern Denial of Human Nature | 0 |
| 0060855925 | The Color of Magic | 0 |
| 1561584029 | The Complete Illustrated Guide to Furniture and Cabinet Construction | 0 |
| 0440237556 | The Dark Highlander | 0 |
| 0471200247 | The Data Warehouse Toolkit: The Complete Guide to Dimensional Modeling | 0 |
| 0345409469 | The Demon-Haunted World: Science As a Candle in the Dark | 0 |
| 0393319407 | The Diversity of Life | 0 |
| 0787960756 | The Five Dysfunctions of a Team: A Leadership Fable | 0 |
| 0679450785 | The Future of Life | 0 |
| 0312287941 | The Girl in the Red Coat: A Memoir | 0 |
| 0446527793 | The Guardian | 0 |
| 0201615762 | The Guru's Guide to Transact-SQL | 0 |
| 0312243022 | The Hours | 0 |
| 0316602051 | The Jester | 0 |
| 0060958332 | The Language Instinct: How the Mind Creates Language | 0 |
| 0316666343 | The Lovely Bones: A Novel | 0 |
| 0156006219 | The Magician's Assistant | 0 |
| 0679722955 | The Names | 0 |
| 156158648X | The New City Home: Smart Solutions for Metro Living | 0 |
| 0446676098 | The Notebook | 0 |
| 0735712360 | The Photoshop Book for Digital Photographers | 0 |
| 0312311354 | The Pianist | 0 |
| 1590520734 | The Rescuer: The O'Malley Series | 0 |
| 0743206061 | The Second Time Around | 0 |
| 0142001740 | The Secret Life of Bees | 0 |
| 0345452089 | The Vampire's Violin | 0 |
| 0743222008 | The Vanished Man: A Lincoln Rhyme Novel | 0 |
| 0066214750 | Twelve Times Blessed | 0 |
| 0684848155 | UNDERWORLD: A NOVEL | 0 |
| 0061161721 | Unseen Academicals | 0 |
| 0140077022 | White Noise | 0 |
| 1880418568 | Wolves of the Calla | 0 |
| 0060958405 | Words and Rules: The Ingredients of Language | 0 |

108 row(s).

## (j) Titles and sales revenue, including unsold books.

| ISBN | Title | Revenue |
| --- | --- | --- |
| 1579550088 | A New Kind of Science | 89.9 |
| 0471288217 | A Visual Dictionary of Architecture | 39.95 |
| 0394739698 | A Field Guide to American Houses | 24.95 |
| 0060502935 | Going Postal | 23.97 |
| 0061020656 | Pyramids | 23.97 |
| 0061020648 | Guards! Guards! | 15.98 |
| 0446608955 | A Walk to Remember | 0.0 |
| 0072222743 | A+ Certification All-in-One Exam Guide | 0.0 |
| 0782140114 | Access 2002 Developer's Handbook Set | 0.0 |
| 0324107501 | Advanced Accounting | 0.0 |
| 0385494246 | Amsterdam | 0.0 |
| 0072315318 | Analysis for Financial Management | 0.0 |
| 0471286168 | Architecture: Form, Space, and Order | 0.0 |
| 038572179X | Atonement | 0.0 |
| 0060934417 | Bel Canto: A Novel | 0.0 |
| 0471391123 | Beyond Coso : Internal Control to Enhance Corporate Governance | 0.0 |
| 0399149848 | Birthright | 0.0 |
| 0385494327 | Black Dogs | 0.0 |
| 0345336895 | Broca's Brain: Reflections on the Romance of Science | 0.0 |
| 0471358983 | Building Construction Illustrated | 0.0 |
| 1561586196 | Building a Shed | 0.0 |
| 1586851357 | Cabins & Camps | 0.0 |
| 0425188361 | Cerulean Sins | 0.0 |
| 0399149392 | Chesapeake Blue | 0.0 |
| 1579902944 | Choosing & Using Hand Tools | 0.0 |
| 0321125169 | ColdFusion MX Web Application Construction Kit | 0.0 |
| 0517576600 | Color: Natural Palettes for Painted Rooms | 0.0 |
| 0865659982 | Composers' Houses | 0.0 |
| 067976867X | Consilience: The Unity of Knowledge | 0.0 |
| 0671004107 | Contact | 0.0 |
| 0743244249 | Cosmopolis: A Novel | 0.0 |
| 0375508325 | Cosmos | 0.0 |
| 0972263608 | Creating Documents with BusinessObjects 5.1 | 0.0 |
| 1558605525 | Data Mining: Practical Machine Learning Tools and Techniques with Java Implementations | 0.0 |
| 0743467523 | Dreamcatcher | 0.0 |
| 0262232197 | Econometric Analysis of Cross Section and Panel Data | 0.0 |
| 0385494149 | Enduring Love | 0.0 |
| 0373218192 | Engaging The Enemy | 0.0 |
| 0743457358 | Everything's Eventual: 14 Dark Tales | 0.0 |
| 0609610570 | Execution: The Discipline of Getting Things Done | 0.0 |
| 0072294337 | Financial Markets & Corporate Strategy | 0.0 |
| 0262024829 | Financial Modeling | 0.0 |
| 0130323519 | Financial Reporting and Analysis | 0.0 |
| 0805317554 | Fundamentals of Database Systems | 0.0 |
| 0596004478 | Google Hacks | 0.0 |
| 0375703764 | House of Leaves | 0.0 |
| 0072227710 | How To Do Everything with Your Tablet PC | 0.0 |
| 0393318486 | How the Mind Works | 0.0 |
| 0471363049 | Intermediate Accounting | 0.0 |
| 0324113641 | Introductory Econometrics: A Modern Approach | 0.0 |
| 0071414339 | Investing in Fixer-Uppers : A Complete Guide to Buying Low, Fixing Smart, Adding Value, and Selling (or Renting) High | 0.0 |
| 0312276702 | Jinn: A Novel | 0.0 |
| 1565924916 | Ldap System Administration | 0.0 |
| 0373272839 | Letters to Kelly | 0.0 |
| 0738206679 | Linked: The New Science of Networks | 0.0 |
| 0373218257 | Love By Design | 0.0 |
| 0316096199 | Lucky: A Memoir | 0.0 |
| 0385504470 | Lullaby: A Novel | 0.0 |
| 0735713170 | Mac OS X v. 10.2 Jaguar Killer Tips | 0.0 |
| 0446606812 | Message in a Bottle | 0.0 |
| 0735712123 | MySQL | 0.0 |
| 0262521415 | Numerical Techniques in Finance | 0.0 |
| 0782140661 | OCP: Oracle9i Certification Kit | 0.0 |
| 0684843285 | ON FOOD AND COOKING | 0.0 |
| 067463442X | On Human Nature | 0.0 |
| 0743455967 | On Writing | 0.0 |
| 0345376595 | Pale Blue Dot: A Vision of the Human Future in Space | 0.0 |
| 0060540753 | Patron Saint of Liars | 0.0 |
| 1558606432 | Persuasive Technology: Using Computers to Change What We Think and Do | 0.0 |
| 0735712379 | Photoshop 7 Down & Dirty Tricks | 0.0 |
| 1586851322 | Prefab | 0.0 |
| 1861004486 | Professional SQL Server 2000 Programming | 0.0 |
| 0130998516 | Real World FPGA Design with Verilog | 0.0 |
| 0072227885 | SQL Server 2000 for Experienced DBA's | 0.0 |
| 0061092177 | Small Gods | 0.0 |
| 0670031518 | The Blank Slate: The Modern Denial of Human Nature | 0.0 |
| 0060855925 | The Color of Magic | 0.0 |
| 1561584029 | The Complete Illustrated Guide to Furniture and Cabinet Construction | 0.0 |
| 0440237556 | The Dark Highlander | 0.0 |
| 0471200247 | The Data Warehouse Toolkit: The Complete Guide to Dimensional Modeling | 0.0 |
| 0345409469 | The Demon-Haunted World: Science As a Candle in the Dark | 0.0 |
| 0393319407 | The Diversity of Life | 0.0 |
| 0787960756 | The Five Dysfunctions of a Team: A Leadership Fable | 0.0 |
| 0679450785 | The Future of Life | 0.0 |
| 0312287941 | The Girl in the Red Coat: A Memoir | 0.0 |
| 0446527793 | The Guardian | 0.0 |
| 0201615762 | The Guru's Guide to Transact-SQL | 0.0 |
| 0312243022 | The Hours | 0.0 |
| 0316602051 | The Jester | 0.0 |
| 0060958332 | The Language Instinct: How the Mind Creates Language | 0.0 |
| 0316666343 | The Lovely Bones: A Novel | 0.0 |
| 0156006219 | The Magician's Assistant | 0.0 |
| 0679722955 | The Names | 0.0 |
| 156158648X | The New City Home: Smart Solutions for Metro Living | 0.0 |
| 0446676098 | The Notebook | 0.0 |
| 0735712360 | The Photoshop Book for Digital Photographers | 0.0 |
| 0312311354 | The Pianist | 0.0 |
| 1590520734 | The Rescuer: The O'Malley Series | 0.0 |
| 0743206061 | The Second Time Around | 0.0 |
| 0142001740 | The Secret Life of Bees | 0.0 |
| 0345452089 | The Vampire's Violin | 0.0 |
| 0743222008 | The Vanished Man: A Lincoln Rhyme Novel | 0.0 |
| 0066214750 | Twelve Times Blessed | 0.0 |
| 0684848155 | UNDERWORLD: A NOVEL | 0.0 |
| 0061161721 | Unseen Academicals | 0.0 |
| 0140077022 | White Noise | 0.0 |
| 1880418568 | Wolves of the Calla | 0.0 |
| 0060958405 | Words and Rules: The Ingredients of Language | 0.0 |

108 row(s).

## (k) All authors tied for the most copies sold.

| AuthorID | FirstName | MiddleName | LastName | CopiesSold |
| --- | --- | --- | --- | --- |
| 101 | Terry |  | Pratchett | 8 |

1 row(s).

## (l) All authors tied for greatest sales revenue.

| AuthorID | FirstName | MiddleName | LastName | Revenue |
| --- | --- | --- | --- | --- |
| 49 | Stephen |  | Wolfram | 89.9 |

1 row(s).

## (m) Customers who purchased a book by any highest-revenue author.

| CustomerID | FirstName | LastName |
| --- | --- | --- |
| 2 | Casey | Morgan |

1 row(s).

## (n) Authors of books purchased by the high-spenders identified in (h).

| AuthorID | FirstName | MiddleName | LastName |
| --- | --- | --- | --- |
| 54 | Lee |  | McAlester |
| 53 | Virginia |  | McAlester |
| 101 | Terry |  | Pratchett |
| 49 | Stephen |  | Wolfram |

4 row(s).
