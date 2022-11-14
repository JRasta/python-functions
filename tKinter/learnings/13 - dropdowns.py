from tkinter import *
from PIL import ImageTk, Image

# creating a root widget (window)
root = Tk()
root.title('Icons, Images, Exit Button(s)')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
root.geometry('400x400')

# setup default option
clicked = StringVar()
clicked.set('Monday')

# create dropdown menu items
drop = OptionMenu(root, clicked, 'Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday')
drop.pack()

# create a mainloop to run the root widget
root.mainloop()
