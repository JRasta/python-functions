from tkinter import *
from PIL import ImageTk, Image

# creating a root widget (window)
root = Tk()
root.title('New Window(s)')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
img = ''


def open_window():
    global img
    top = Toplevel()
    top.title('Second Window')
    top.iconbitmap('..\\misc\\tech.ico')
    img = ImageTk.PhotoImage(Image.open('..\\misc\\aland.png'))
    Label(top, image=img).pack()


Button(root, text='Open 2nd Window', command=open_window).pack()

# create a mainloop to run the root widget
root.mainloop()
