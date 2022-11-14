from tkinter import *
from tkinter import messagebox

# creating a root widget (window)
root = Tk()
root.title('Message Boxes')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon

"""
Different message popups available:
- showinfo
- showwarning
- showerror
- askquestion
- askokcancel
- askyesno
"""

def info():
    response = messagebox.showinfo("Title", "Popup message")
    lbl = Label(root, text=response)
    lbl.pack()


def warning():
    response = messagebox.showwarning("Title", "Popup message")
    lbl = Label(root, text=response)
    lbl.pack()


def error():
    response = messagebox.showerror("Title", "Popup message")
    lbl = Label(root, text=response)
    lbl.pack()


def askquestion():
    response = messagebox.askquestion("Title", "Popup message")
    lbl = Label(root, text=response)
    lbl.pack()


def askokcancel():
    response = messagebox.askokcancel("Title", "Popup message")
    lbl = Label(root, text=response)
    lbl.pack()


def askyesno():
    response = messagebox.askyesno("Title", "Popup message")
    lbl = Label(root, text=response)
    lbl.pack()


"""
Multiple buttons showcasing the different popups
"""

button = Button(root, text='Info Popup', command=info)
button.pack()

button = Button(root, text='Warning Popup', command=warning)
button.pack()

button = Button(root, text='Error Popup', command=error)
button.pack()

button = Button(root, text='Ask Question Popup', command=askquestion)
button.pack()

button = Button(root, text='Ask OK | Cancel Popup', command=askokcancel)
button.pack()

button = Button(root, text='Ask Yes | No Popup', command=askyesno)
button.pack()


# create a mainloop to run the root widget
root.mainloop()
