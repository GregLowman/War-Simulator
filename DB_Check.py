"""Query and print all rows from the WarSimulation players table."""
import sqlite3

db = sqlite3.connect("WarSimulation.sqlite")

for row in db.execute('SELECT * from players'):
    print(row)

db.close()
