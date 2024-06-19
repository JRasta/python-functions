import sqlite3

# Create database
conn = sqlite3.connect("customer.db")

# Create cursor
c = conn.cursor()

# Query Database
c.execute("""SELECT * FROM customers""")

print("Fetch First Table Entry", c.fetchone())
print("Printing first four table entries", c.fetchmany(4))
print("Printing all table entries", c.fetchall())

# Commit our command
conn.commit()

# Close connection - BEST PRACTICE
conn.close()