from tkinter import *

# creating a root widget (window)
root = Tk()

# extra input parameters:
# e = Entry(root, width=50)
# e = Entry(root, bg='blue')
# e = Entry(root, fg='white')
# e = Entry(root, borderwidth=5)
e = Entry(root, width=50)
e.pack()

# set placeholder text for input field
e.insert(0, 'Enter your name')


def my_click():
    # e.get() function gets the user entered input
    my_label = Label(root, text=f'Hello {e.get()}')
    my_label.pack()


# creating a button widget
myButton = Button(root, text='Enter your name', command=my_click)
myButton.pack()

# create a mainloop to run the root widget
root.mainloop()
