import sqlite3

connection = sqlite3.connect(('calc-app-db.db'))

c=connection.cursor()

c.execute("INSERT INTO past_calculations (num1,num2,operation,result,timestamp) VALUES (4, 6, '-', -2, '2020-02-12')")
c.execute("SELECT * FROM past_calculations")
print(c.fetchall())

connection.commit()
connection.close()
