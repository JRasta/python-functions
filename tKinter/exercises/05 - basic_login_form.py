""" A simple Login screen
Author: Code First with Hala
Date: 2023
Reason: Educational
"""

from tkinter import *
from tkinter import messagebox

def login():
    username = 'johnsmith'
    password = '12345'

    if username_input.get() == username and password_input.get() == password:
        messagebox.showinfo(title='Login Success', message='You successfully logged in!!')
    else:
        messagebox.showerror(title='Login Failed', message='User or Password is incorrect!!')


# creating a root widget (window)
root = Tk()
root.title('Login Form')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
root.geometry('800x500')
root.configure(bg='#333333')

# create a frame for responsive GUI
frame = Frame(root, bg='#333333')

# create & place widgets
login_lbl = Label(frame, text='Login', bg='#333333', fg='#ff0000', font=('Arial', 30))
login_lbl.grid(row=0, column=0, columnspan=2, sticky='news', pady=40)

username_lbl = Label(frame, text='Username', bg='#333333', fg='#ffffff', font=('Arial', 16))
username_lbl.grid(row=1, column=0)

username_input = Entry(frame, width='20', borderwidth='2', font=('Arial', 16))
username_input.grid(row=1, column=1, pady=20)

password_lbl = Label(frame, text='Password', bg='#333333', fg='#ffffff', font=('Arial', 16))
password_lbl.grid(row=2, column=0)

password_input = Entry(frame, width='20', borderwidth='2', show='*', font=('Arial', 16))
password_input.grid(row=2, column=1, pady=20)

login_btn = Button(frame, text='Login', bg='#ff0000', fg='#ffffff', font=('Arial', 16), command=lambda: login())
login_btn.grid(row=3, column=0, columnspan=2, pady=30)

# show frame
frame.pack()

# create a mainloop to run the root widget
root.mainloop()
