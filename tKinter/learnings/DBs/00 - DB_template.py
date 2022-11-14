from tkinter import *
from PIL import ImageTk, Image
import sqlite3

# creating a root widget (window)
root = Tk()
root.title('Icons, Images, Exit Button(s)')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
root.geometry('400x400')

# database
conn = sqlite3.connect('../address_book.db')

# commit changes to db
conn.commit()

# close connection
conn.close()

# create a mainloop to run the root widget
root.mainloop()
