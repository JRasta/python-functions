from tkinter import *

# creating a root widget (window)
root = Tk()

def myClick():
    my_label = Label(root, text='Button worked!')
    my_label.pack()


# creating a button widget
myButton = Button(root, text='Click Me!', state=DISABLED)

# fg & bg will accept a hex color code
myButton2 = Button(root, text='Click Me!', padx=50, command=myClick, fg='blue')
myButton3 = Button(root, text='Click Me!', pady=50, bg='#ff0000')

# add to root widget
myButton.pack()
myButton2.pack()
myButton3.pack()

# create a mainloop to run the root widget
root.mainloop()
