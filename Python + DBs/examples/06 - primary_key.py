import sqlite3

# Create database
conn = sqlite3.connect("customer.db")

# Create cursor
c = conn.cursor()

# Query Database
c.execute("""SELECT rowid, * FROM customers""")

# Fetch all records
items = c.fetchall()
for i in items:
    print(i)

# Commit our command
conn.commit()

# Close connection - BEST PRACTICE
conn.close()