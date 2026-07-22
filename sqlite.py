import sqlite3
import pandas as pd

conn = sqlite3.connect('cricket.db')
cursor = conn.cursor()

cursor.executescript("""
DROP TABLE IF EXISTS Team;
DROP TABLE IF EXISTS Match;
DROP TABLE IF EXISTS Player_Match;

CREATE TABLE Team(
    Team_Nname  TNTEGER PRIMARY KEY,
    Team_Id   
);

CREATE TABLE Match (
    Match_Id     ITNTEGER PRIMARY KEY,
    Season_Id    INTEAGER,
    Match_Winter INTEAGER,
    Win_Margin   INTEAGER
);
                     
CREATE TABLE Player_Match (
    Match_Id     ITNTEGER, 
    Player_Id    INTEAGER
);
                     
INSERT INTO TEAM VALUES
  (1, 'Lahore Qalandars'),(2, 'Islamabad United'),
  (3, 'Peshawar Zalmi'),
                     
INSERT INTO MATCH VALUES
  (1,7,5,35),(2,7,5,22),(3,8,5,45)

INSERT INTO Player_Match VALUES 
  (1,101),(1,102),(2,103)
""")

conn.commit()
print('Database redy!')


tables = pd.read_sql("""SELECT * 
    FROM Match;""",conn)
print(matches)
print('Rows and columns:', matches.shape)