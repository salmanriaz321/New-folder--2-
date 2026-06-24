CREATE TABLE IF NOT EXISTS Salesman (
    Salesman_id TEXT PRIMARY KEY,
    name TEXT,
    city TEXT,
    comission REAL
);

INSERT INTO Salesman (Salesman_id, name, city, comission) VALUES
('5001', 'James Hoog', 'New York', 0.15),
('5007', 'Paul Adam', 'Rome', 0.13);

SELECT * FROM Salesman;

CREATE TABLE IF NOT EXISTS Orders (
    ord_no TEXT PRIMARY KEY,
    purch_amt REAL,
    customer_id TEXT,
    Salesman_id TEXT
);
INSERT INTO Orders( ord_no, purch_amt, customer_id, Salesman_id) VALUES
('70007', 948.5, '2012-09-10', '3005', '5005'),
('70005', 928.5, '2012-08-20', '3007', '5008');
