CREATE TABLE IF NOT EXISTS CRICKETWORLDCUP(
    ID INT,
    NAME VARCHAR(100),
    shirtnumber INT, 
    TEAM TEXT,
    score TEXT
); 

INSERT INTO CRICKETWORLDCUP (ID, NAME, shirtnumber, TEAM, score)
VALUES
('21', 'Babar Azam', '56', 'Pakistan', '200-3'),
('16', 'Virat Kholi', '18', 'India', '180-4'),
('20', 'Mitchel Starc', '10', 'Australia', '150-9');

SELECT COUNT(SCORE) AS total_SC FROM CRICKETWORLDCUP;
SELECT TEAM, score FROM CRICKETWORLDCUP ORDER BY score ASC LIMIT 5;