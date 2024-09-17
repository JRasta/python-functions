import sqlite3

# Create database
conn = sqlite3.connect("customer.db")

# Create cursor
c = conn.cursor()

# Create a table
# DOC string  RECOMMENDED!!
c.execute("""CREATE TABLE customers (first_name TEXT, last_name TEXT, email_address TEXT)""")

# Commit our command
conn.commit()

# Close connection - BEST PRACTICE
conn.close()