import sqlite3
import emailsender

db = sqlite3.connect('MyFirstSQLApp')
cursor = db.cursor()

cursor.execute("SELECT email FROM users ORDER BY id")

row = cursor.fetchone()
while row is not None:
    emailsender.send_email(str(row[0]))
    row = cursor.fetchone()

db.close()
print("Success")