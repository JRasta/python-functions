from tkinter import *
import sqlite3

# creating a root widget (window)
root = Tk()
root.title('Databases')
root.iconbitmap('..\\..\\misc\\tech.ico')  # add user defined icon
root.geometry('400x400')

# database
conn = sqlite3.connect('address_book.db')

# create cursor
c = conn.cursor()

# triple quotes for multiple lines in writing SQL in python
c.execute("""CREATE TABLE addresses(
           first_name text,
           last_name text,
           address text,
           city text,
           state text,
           zipcode integer)""")

# commit changes to db
conn.commit()

# close connection
conn.close()

# create a mainloop to run the root widget
root.mainloop()
