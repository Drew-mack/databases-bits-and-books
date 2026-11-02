SQLite format 3

-- (a)
SELECT	B.Title, B.Price
	FROM	Book AS B, Writes AS W, Author AS A
	WHERE	B.ISBN = W.WISBN
			AND W.WAuthorID = A.AuthorID
			AND A.FirstName = 'Terry'
			AND A.LastName = 'Pratchett'
			AND B.Price < 10
	ORDER BY	B.Title;

-- (b)
SELECT	B.Title, O.OrderDate AS PurchaseDate
	FROM	Customer AS C, Orders AS O, Order_Item AS I, Book AS B
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
			AND I.OISBN = B.ISBN
			AND C.Email = 'email_example'
	ORDER BY	O.OrderDate, B.Title;

-- (c)
SELECT	B.Title, B.ISBN, B.StockQuantity
	FROM	Book AS B
	WHERE	B.StockQuantity < 5
	ORDER BY	B.StockQuantity, B.Title;

-- (d)
SELECT	DISTINCT C.FirstName, C.LastName, B.Title
	FROM	Customer AS C, Orders AS O, Order_Item AS I, Book AS B,
			Writes AS W, Author AS A
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
			AND I.OISBN = B.ISBN
			AND B.ISBN = W.WISBN
			AND W.WAuthorID = A.AuthorID
			AND A.FirstName = 'Terry'
			AND A.LastName = 'Pratchett'
	ORDER BY	C.LastName, C.FirstName, B.Title;

-- (e)
SELECT	C.FirstName, C.LastName, SUM(I.Quantity) AS TotalBooks
	FROM	Customer AS C, Orders AS O, Order_Item AS I
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
			AND C.Email = 'email_example'
	GROUP BY	C.CustomerID, C.FirstName, C.LastName;

-- (f)
SELECT	C.FirstName, C.LastName, SUM(I.Quantity) AS TotalBooks
	FROM	Customer AS C, Orders AS O, Order_Item AS I
	WHERE	C.CustomerID = O.OCustomerID
			AND O.OrderID = I.OOrderID
	GROUP BY	C.CustomerID, C.FirstName, C.LastName
	ORDER BY	TotalBooks DESC