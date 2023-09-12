""" A simple quiz via a GUI
Author: FreeCodeAcademy
Date: 2022
"""

from tkinter import *

# creating a root widget (window)
root = Tk()
root.title('Spot Quiz')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
root.geometry('400x230')

a = IntVar()

# question frame
q_frame = LabelFrame(root, text=' Question 1: ', borderwidth=0, highlightthickness=0)
q_frame.pack(padx=20, pady=20, anchor=W)

question = Label(q_frame, text=' Lenin died on the 21st January but what was the year? ')
question.pack(pady=3)

# answer frame
a_frame = LabelFrame(root, text=' Answers: ', borderwidth=0, highlightthickness=0)
a_frame.pack(padx=20, pady=5, anchor=W)

def update():
    lbl = Label(root, text=a.get())
    lbl.pack()


a1 = Radiobutton(a_frame, text='1924', variable=a, value=1, command=update)
a1.pack(anchor=W)
a2 = Radiobutton(a_frame, text='1934', variable=a, value=2, command=update)
a2.pack(anchor=W)
a3 = Radiobutton(a_frame, text='1944', variable=a, value=3, command=update)
a3.pack(anchor=W)
a4 = Radiobutton(a_frame, text='1954', variable=a, value=4, command=update)
a4.pack(anchor=W)


# create a mainloop to run the root widget
root.mainloop()
