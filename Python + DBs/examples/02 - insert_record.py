import sqlite3

# Create database
conn = sqlite3.connect("customer.db")

# Create cursor
c = conn.cursor()

# Create a table
# DOC string  RECOMMENDED!!
c.execute("""INSERT INTO customers VALUES (
    'John',
    'Smith',
    'jayts4k@gmail.com'
    )""")

c.execute("""INSERT INTO customers VALUES (
    'James',
    'Brown',
    'jbrown12345@gmail.com'
    )""")

c.execute("""INSERT INTO customers VALUES (
    'Knee',
    'Legs',
    'kneesmall1234@gmail.com'
    )""")

# Commit our command
conn.commit()

# Close connection - BEST PRACTICE
conn.close()