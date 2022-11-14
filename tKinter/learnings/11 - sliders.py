import time
from tkinter import *
from PIL import ImageTk, Image

# creating a root widget (window)
root = Tk()
root.title('Sliders')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
root.geometry("400x400")  # set the size of the window

def slide():
    global lbl
    lbl = Label(root, text=horizontal.get())
    lbl.pack()
    root.geometry(str(horizontal.get()) + "x" + str(vertical.get()))


# vertical slider
vertical = Scale(root, from_=0, to=400)  # pack needs to be separate
vertical.pack()

# horizontal slider
horizontal = Scale(root, from_=0, to=400, orient=HORIZONTAL)  # pack needs to be separate
horizontal.pack()

# label to display horizontal data
lbl = Label(root, text=horizontal.get())
lbl.pack()

# update slider info
btn = Button(root, text='Update', command=slide)
btn.pack()

# create a mainloop to run the root widget
root.mainloop()
