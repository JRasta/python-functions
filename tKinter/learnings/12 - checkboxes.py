from tkinter import *
from PIL import ImageTk, Image

# creating a root widget (window)
root = Tk()
root.title('Icons, Images, Exit Button(s)')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
root.geometry('400x400')

var1 = IntVar()

def show():
    global lbl
    lbl = Label(root, text=var1.get())
    lbl.pack()


c = Checkbutton(root, text='Check this box!', variable=var1)
c.pack()

lbl = Label(root, text=var1.get())
lbl.pack()

btn = Button(root, text='Update', command=show)
btn.pack()

# create a mainloop to run the root widget
root.mainloop()
