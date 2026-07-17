import sqlite3
database = 'database.sqlite'
conn = sqlite3.connect(database)
print('Opened data succsessfully')
import pandas as pd
tables = pd.read_sql("""SELECT * 
                    FROM sqlite_ master
                     WHERE type='table';""", conn)
tables