from tkinter import *

# creating a root widget (window)
root = Tk()

# creating a label widget
# without the OOP grid attached
myLabel1 = Label(root, text='Hello World')
myLabel2 = Label(root, text='My name is, my name is...')

# creating a label widget
# with the OOP grid attached
Label(root, text='Hello bob').grid(row=1, column=2)
Label(root, text='Goodbye Billy').grid(row=2, column=0)

# Adding label widget to the root widget
myLabel1.grid(row=0, column=0)
myLabel2.grid(row=1, column=1)

# create a mainloop to run the root widget
root.mainloop()
