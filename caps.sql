CREATE TABLE IF NOT EXISTS CRICKET(
    ID INTEGER,
    NAME VARCHAR(100),
    shirtnumber INT, 
    TEAM TEXT,
    score TEXT
); 

INSERT INTO CRICKET( ID, NAME, shirtnumber, TEAM, score)
VALUES

('17', 'Rashid Khan', '19', 'Afganistan', '6-38'),
('36', 'Bryme Lara', '10', 'West Indies', '250-0');
SELECT  * FROM CRICKET WHERE ID IS NULL;
SELECT  * FROM CRICKET WHERE ID BETWEEN 17 AND 36;
