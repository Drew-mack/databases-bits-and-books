-- All recorded orders count as purchases. Revenue for a coauthored book is
-- credited in full to each author. Customer averages include customers with
-- no orders at $0. Customer-specific questions use a stable sample email.

-- (a) Titles of Terry Pratchett books priced below $10.
SELECT DISTINCT b.Title FROM Book b JOIN Writes w ON w.WISBN=b.ISBN JOIN Author a ON a.AuthorID=w.WAuthorID WHERE a.FirstName='Terry' AND a.LastName='Pratchett' AND b.Price < 10 ORDER BY b.Title;

-- (b) Titles and purchase dates for Avery Reader.
SELECT b.Title, o.OrderDate FROM Customer c JOIN Orders o ON o.OCustomerID=c.CustomerID JOIN Order_Item i ON i.OOrderID=o.OrderID JOIN Book b ON b.ISBN=i.OISBN WHERE c.Email='avery.reader@example.com' ORDER BY o.OrderDate,b.Title;

-- (c) Titles and ISBNs with fewer than five copies.
SELECT Title, ISBN FROM Book WHERE StockQuantity < 5 ORDER BY Title, ISBN;

-- (d) Customers and titles for purchases of Terry Pratchett books.
SELECT DISTINCT c.CustomerID,c.FirstName,c.LastName,b.Title FROM Customer c JOIN Orders o ON o.OCustomerID=c.CustomerID JOIN Order_Item i ON i.OOrderID=o.OrderID JOIN Book b ON b.ISBN=i.OISBN JOIN Writes w ON w.WISBN=b.ISBN JOIN Author a ON a.AuthorID=w.WAuthorID WHERE a.FirstName='Terry' AND a.LastName='Pratchett' ORDER BY c.CustomerID,b.Title;

-- (e) Copies purchased by Avery Reader, including zero if no purchases.
SELECT c.CustomerID,c.FirstName,c.LastName,COALESCE(SUM(i.Quantity),0) AS TotalBooks FROM Customer c LEFT JOIN Orders o ON o.OCustomerID=c.CustomerID LEFT JOIN Order_Item i ON i.OOrderID=o.OrderID WHERE c.Email='avery.reader@example.com' GROUP BY c.CustomerID;

-- (f) All customers tied for the most copies purchased.
WITH totals AS (SELECT c.CustomerID,c.FirstName,c.LastName,COALESCE(SUM(i.Quantity),0) AS TotalBooks FROM Customer c LEFT JOIN Orders o ON o.OCustomerID=c.CustomerID LEFT JOIN Order_Item i ON i.OOrderID=o.OrderID GROUP BY c.CustomerID) SELECT * FROM totals WHERE TotalBooks=(SELECT MAX(TotalBooks) FROM totals) ORDER BY CustomerID;

-- (g) Total spending by every customer, including those with no orders.
SELECT c.CustomerID,c.FirstName,c.LastName,ROUND(COALESCE(SUM(i.Quantity*i.UnitPrice),0),2) AS TotalSpent FROM Customer c LEFT JOIN Orders o ON o.OCustomerID=c.CustomerID LEFT JOIN Order_Item i ON i.OOrderID=o.OrderID GROUP BY c.CustomerID ORDER BY c.CustomerID;

-- (h) Customers spending more than the average across all customers.
WITH totals AS (SELECT c.CustomerID,c.FirstName,c.LastName,ROUND(COALESCE(SUM(i.Quantity*i.UnitPrice),0),2) AS TotalSpent FROM Customer c LEFT JOIN Orders o ON o.OCustomerID=c.CustomerID LEFT JOIN Order_Item i ON i.OOrderID=o.OrderID GROUP BY c.CustomerID) SELECT * FROM totals WHERE TotalSpent>(SELECT AVG(TotalSpent) FROM totals) ORDER BY TotalSpent DESC,CustomerID;

-- (i) Titles and copies sold, including unsold books.
SELECT b.ISBN,b.Title,COALESCE(SUM(i.Quantity),0) AS CopiesSold FROM Book b LEFT JOIN Order_Item i ON i.OISBN=b.ISBN GROUP BY b.ISBN ORDER BY CopiesSold DESC,b.Title,b.ISBN;

-- (j) Titles and sales revenue, including unsold books.
SELECT b.ISBN,b.Title,ROUND(COALESCE(SUM(i.Quantity*i.UnitPrice),0),2) AS Revenue FROM Book b LEFT JOIN Order_Item i ON i.OISBN=b.ISBN GROUP BY b.ISBN ORDER BY Revenue DESC,b.Title,b.ISBN;

-- (k) All authors tied for the most copies sold.
WITH totals AS (SELECT a.AuthorID,a.FirstName,a.MiddleName,a.LastName,COALESCE(SUM(i.Quantity),0) AS CopiesSold FROM Author a LEFT JOIN Writes w ON w.WAuthorID=a.AuthorID LEFT JOIN Order_Item i ON i.OISBN=w.WISBN GROUP BY a.AuthorID) SELECT * FROM totals WHERE CopiesSold=(SELECT MAX(CopiesSold) FROM totals) ORDER BY AuthorID;

-- (l) All authors tied for greatest sales revenue.
WITH totals AS (SELECT a.AuthorID,a.FirstName,a.MiddleName,a.LastName,ROUND(COALESCE(SUM(i.Quantity*i.UnitPrice),0),2) AS Revenue FROM Author a LEFT JOIN Writes w ON w.WAuthorID=a.AuthorID LEFT JOIN Order_Item i ON i.OISBN=w.WISBN GROUP BY a.AuthorID) SELECT * FROM totals WHERE Revenue=(SELECT MAX(Revenue) FROM totals) ORDER BY AuthorID;

-- (m) Customers who purchased a book by any highest-revenue author.
WITH totals AS (SELECT w.WAuthorID,ROUND(SUM(i.Quantity*i.UnitPrice),2) AS Revenue FROM Writes w JOIN Order_Item i ON i.OISBN=w.WISBN GROUP BY w.WAuthorID), top_authors AS (SELECT WAuthorID FROM totals WHERE Revenue=(SELECT MAX(Revenue) FROM totals)) SELECT DISTINCT c.CustomerID,c.FirstName,c.LastName FROM Customer c JOIN Orders o ON o.OCustomerID=c.CustomerID JOIN Order_Item i ON i.OOrderID=o.OrderID JOIN Writes w ON w.WISBN=i.OISBN JOIN top_authors t ON t.WAuthorID=w.WAuthorID ORDER BY c.CustomerID;

-- (n) Authors of books purchased by the high-spenders identified in (h).
WITH totals AS (SELECT c.CustomerID,ROUND(COALESCE(SUM(i.Quantity*i.UnitPrice),0),2) AS TotalSpent FROM Customer c LEFT JOIN Orders o ON o.OCustomerID=c.CustomerID LEFT JOIN Order_Item i ON i.OOrderID=o.OrderID GROUP BY c.CustomerID), high_spenders AS (SELECT CustomerID FROM totals WHERE TotalSpent>(SELECT AVG(TotalSpent) FROM totals)) SELECT DISTINCT a.AuthorID,a.FirstName,a.MiddleName,a.LastName FROM high_spenders h JOIN Orders o ON o.OCustomerID=h.CustomerID JOIN Order_Item i ON i.OOrderID=o.OrderID JOIN Writes w ON w.WISBN=i.OISBN JOIN Author a ON a.AuthorID=w.WAuthorID ORDER BY a.LastName,a.FirstName,a.AuthorID;
