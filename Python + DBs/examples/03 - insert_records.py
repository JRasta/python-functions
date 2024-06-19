import sqlite3

# Create database
conn = sqlite3.connect("customer.db")

# Create cursor
c = conn.cursor()

# Customer list
customer = [('Eliseo', 'Valen', 'eliseo@gmail.com'), ('Wayne', 'Thomas', 'wayne@gmail.com'),
            ('Adolph', 'Pitts', 'adolph@gmail.com'), ('Byron', 'Esteste', 'byron@gmail.com'),
            ('Todd', 'Sanders', 'todd@gmail.com'), ('Sydney', 'Conley', 'sydney@gmail.com')]

# Create a table
# DOC string  RECOMMENDED!!
c.executemany("""INSERT INTO customers VALUES (?,?,?)""", customer)

# Commit our command
conn.commit()

# Close connection - BEST PRACTICE
conn.close()