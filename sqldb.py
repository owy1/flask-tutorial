import sqlite3

conn = sqlite3.connect('database.db')
print "opened database successfully";

conn.execute('''DROP TABLE students''')

conn.execute('CREATE TABLE students (name TEXT, addr TEXT, city TEXT, pin TEXT)')
print "table created successfully";
conn.close()