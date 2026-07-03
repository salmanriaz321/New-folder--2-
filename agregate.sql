CREATE TABLE IF NOT EXISTS WORLDCUP(
    ID int,
NAME VARCHAR (2014),
shirtnumber int, 
TEAM text,
score text
); 
INSERT INTO WORLDCUP ( ID, NAME, SHIRTNUMBER, TEAM, SCORE)
VALUES
( '14', 'NEYMAR jr', '10', 'Brazil', '5-0'),
( '8', 'RONALDO', '7', 'Portugal', '4-0' ),
( '21', 'MESSI', '10', 'Argentina', '3-0' );
SELECT COUNT(SCORE) AS total_SC FROM WORLDCUP;
