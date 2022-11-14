from tkinter import *

# creating a root widget (window)
root = Tk()
root.title('Radio Button(s)')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon

r = IntVar()
r.set(2)

def clicked(value):
    global lbl
    lbl = Label(root, text=value)
    lbl.pack()


# normal declaration
Radiobutton(root, text='Option 1', variable=r, value=1, command=lambda: clicked(r.get())).pack()
Radiobutton(root, text='Option 2', variable=r, value=2, command=lambda: clicked(r.get())).pack()

lbl = Label(root, text=r.get())
lbl.pack()

btn = Button(root, text='Click Me!', command=lambda: clicked(r.get()))
btn.pack()

MODES = [("Pepperoni", "Pepperoni"), ("Cheese", "Cheese"), ("Mushroom", "Mushroom"), ("Onions", "Onions")]

pizza = StringVar()
pizza.set("Pepperoni")

for text, mode in MODES:
    Radiobutton(root, text=text, variable=pizza, value=mode).pack(anchor=W)

lbl = Label(root, text=pizza.get())
lbl.pack()

btn = Button(root, text='Click Me!', command=lambda: clicked(pizza.get()))
btn.pack()

# create a mainloop to run the root widget
root.mainloop()
