import sqlite3

# Create database
conn = sqlite3.connect("customer.db")

# Create cursor
c = conn.cursor()

# Query Database
c.execute("""SELECT * FROM customers""")

items = c.fetchall()

print("NAME " + "\t\t\tEMAIL")
print("----" + "\t\t\t-----")
for i in items:
    print(i[0] + " " + i[1] + "\t" + i[2])

# print(items)

# Commit our command
conn.commit()

# Close connection - BEST PRACTICE
conn.close()