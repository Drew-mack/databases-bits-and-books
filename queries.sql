SQLite format 3

-- (a) Title of all books by Pratchett that cost less than $10
SELECT	B.Title
	FROM	Book AS B, Writes AS W, Author AS A
	WHERE	B.ISBN = W.WISBN
			AND W.WAuthorID = A.AuthorID
			AND A.FirstName = 'Terry'
			AND A.LastName = 'Pratchett'
			AND B.Price < 10;

-- (b) Titles and purchase dates for a single customer
SELECT	B.Title, O.OrderDate
	FROM	Customer AS C, Orders AS O, Order_Item AS I, Book AS B
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
			AND I.OISBN = B.ISBN
			AND C.FirstName = 'FirstName'
			AND C.LastName = 'LastName';

-- (c) Titles and ISBNs for books with less than 5 copies in stock
SELECT	B.Title, B.ISBN
	FROM	Book AS B
	WHERE	B.StockQuantity < 5;

-- (d) Customers who purchased Pratchett books and the titles they bought
SELECT	DISTINCT C.CustomerID, C.FirstName, C.LastName, B.Title
	FROM	Customer AS C, Orders AS O, Order_Item AS I, Book AS B,
			Writes AS W, Author AS A
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
			AND I.OISBN = B.ISBN
			AND B.ISBN = W.WISBN
			AND W.WAuthorID = A.AuthorID
			AND A.FirstName = 'Terry'
			AND A.LastName = 'Pratchett';

-- (e) Total number of books purchased by a single customer
SELECT	C.FirstName, C.LastName, SUM(I.Quantity) AS TotalBooks
	FROM	Customer AS C, Orders AS O, Order_Item AS I
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
			AND C.FirstName = 'FirstName'
			AND C.LastName = 'LastName'
	GROUP BY	C.CustomerID;

-- (f) Customer(s) who purchased the most books and their total
SELECT	C.FirstName, C.LastName, SUM(I.Quantity) AS TotalBooks
	FROM	Customer AS C, Orders AS O, Order_Item AS I
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
	GROUP BY	C.CustomerID
	HAVING SUM(I.Quantity) =
		(SELECT MAX(T.Total)
			FROM	(SELECT SUM(Y.Quantity) AS total
					WHERE O.OrderID = I.OOrderID
					GROUP BY X.OCustomerID));

-- (g) Total dollar amount spent by each customer
SELECT	C.FirstName, C.LastName, SUM(I.Quantity * I.UnitPrice) AS TotalSpent
	FROM	Customer AS C, Orders AS O, Order_Item AS I
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
	GROUP BY	C.CustomerID;

-- (h) Customers who spent more than the average customer (high-spenders)
SELECT	C.FirstName, C.LastName, SUM(I.Quantity * I.UnitPrice) AS TotalSpent
	FROM	Customer AS C, Orders AS O, Order_Item AS I
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
	GROUP BY	C.CustomerID
	HAVING	SUM(I.Quantity * I.UnitPrice) >
			(SELECT SUM(Z.Quantity * Z.UnitPrice) FROM Order_Item AS Z)
			/ (SELECT COUNT(*) FROM Customer AS D);

-- (i) Titles and total copies sold, sorted by popularity
SELECT	B.Title, SUM(I.Quantity) AS CopiesSold
	FROM	Book AS B, Order_Item AS I
	WHERE	B.ISBN = I.OISBN
	GROUP BY	B.ISBN
	ORDER BY	CopiesSold DESC;

-- (j) Titles and total revenue, sorted by profitability
SELECT	B.Title, SUM(I.Quantity * I.UnitPrice) AS Revenue
	FROM	Book AS B, Order_Item AS I
	WHERE	B.ISBN = I.OISBN
	GROUP BY	B.ISBN
	ORDER BY	Revenue DESC;

-- (k) Most popular author(s) (by books sold)
SELECT	A.FirstName, A.MiddleName, A.LastName, SUM(I.Quantity) AS CopiesSold
	FROM	Author AS A, Writes AS W, Order_Item AS I
	WHERE	A.AuthorID = W.WAuthorID
			AND W.WISBN = I.OISBN
	GROUP BY	A.AuthorID
	ORDER BY	CopiesSold DESC
	LIMIT 1;

-- (l) Most profitable author(s) (by revenue)
SELECT	A.FirstName, A.MiddleName, A.LastName,
		SUM(I.Quantity * I.UnitPrice) AS Revenue
	FROM	Author AS A, Writes AS W, Order_Item AS I
	WHERE	A.AuthorID = W.WAuthorID
			AND W.WISBN = I.OISBN
	GROUP BY	A.AuthorID
	ORDER BY	Revenue DESC;
	LIMIT 1;

-- (m) Customers who purchased books by the most profitable author(s)
SELECT	DISTINCT C.CustomerID, C.FirstName, C.LastName
	FROM	Customer AS C, Orders AS O, Order_Item AS I, Writes AS W
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
			AND I.OISBN = W.WISBN
			AND W.WAuthorID IN
				(SELECT X.WAuthorID
					FROM	Writes AS X, Order_Item AS Y
					WHERE	X.WISBN = Y.OISBN
					GROUP BY	X.WAuthorID
					HAVING	ROUND(SUM(Y.Quantity * Y.UnitPrice), 2) =
							(SELECT MAX(T.Revenue)
								FROM	(SELECT ROUND(SUM(Q.Quantity * Q.UnitPrice), 2) AS Revenue
											FROM	Writes AS R, Order_Item AS Q
											WHERE	R.WISBN = Q.OISBN
											GROUP BY	R.WAuthorID) AS T));

-- (n) Authors of books purchased by the high-spender customers (from h.)
SELECT	DISTINCT C.CustomerID, C.FirstName, C.LastName
	FROM	Customer AS C, Orders AS O, Order_Item AS I, Writes AS W
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
			AND I.OISBN = W.WISBN
			AND W.WAuthorID =
				(SELECT X.WAuthorID
					FROM	Writes AS X, Order_Item AS Y
					WHERE	X.WISBN = Y.OISBN
					GROUP BY	X.WAuthorID
					ORDER BY	SUM(Y.Quantity * Y.UnitPrice) DESC
					LIMIT 1);