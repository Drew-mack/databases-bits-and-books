-- (a) Terry Pratchett books priced below $10
SELECT B.Title, B.Price
FROM Book AS B
JOIN Writes AS W ON B.ISBN = W.WISBN
JOIN Author AS A ON W.WAuthorID = A.AuthorID
WHERE A.FirstName = 'Terry' AND A.LastName = 'Pratchett' AND B.Price < 10
ORDER BY B.Title;

-- (b) Purchase history for the selected sample customer
SELECT B.Title, O.OrderDate AS PurchaseDate
FROM Customer AS C
JOIN Orders AS O ON C.CustomerID = O.OCustomerID
JOIN Order_Item AS I ON O.OrderID = I.OOrderID
JOIN Book AS B ON I.OISBN = B.ISBN
WHERE C.Email = 'email_example'
ORDER BY O.OrderDate, B.Title;

-- (c) Books with fewer than five copies in stock
SELECT B.Title, B.ISBN, B.StockQuantity
FROM Book AS B
WHERE B.StockQuantity < 5
ORDER BY B.StockQuantity, B.Title;

-- (d) Customers who purchased Terry Pratchett books
SELECT DISTINCT C.FirstName, C.LastName, B.Title
FROM Customer AS C
JOIN Orders AS O ON C.CustomerID = O.OCustomerID
JOIN Order_Item AS I ON O.OrderID = I.OOrderID
JOIN Book AS B ON I.OISBN = B.ISBN
JOIN Writes AS W ON B.ISBN = W.WISBN
JOIN Author AS A ON W.WAuthorID = A.AuthorID
WHERE A.FirstName = 'Terry' AND A.LastName = 'Pratchett'
ORDER BY C.LastName, C.FirstName, B.Title;

-- (e) Number of books purchased by the selected sample customer
SELECT C.FirstName, C.LastName, SUM(I.Quantity) AS TotalBooks
FROM Customer AS C
JOIN Orders AS O ON C.CustomerID = O.OCustomerID
JOIN Order_Item AS I ON O.OrderID = I.OOrderID
WHERE C.Email = 'email_example'
GROUP BY C.CustomerID, C.FirstName, C.LastName;

-- (f) Number of books purchased by each customer
SELECT C.FirstName, C.LastName, SUM(I.Quantity) AS TotalBooks
FROM Customer AS C
JOIN Orders AS O ON C.CustomerID = O.OCustomerID
JOIN Order_Item AS I ON O.OrderID = I.OOrderID
GROUP BY C.CustomerID, C.FirstName, C.LastName
ORDER BY TotalBooks DESC;
