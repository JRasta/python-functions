""" A simple URL shortener
Author: Code First with Hala
Date: 2023
Reason: Educational
"""

import time
import pyshorteners

from tkinter import *
from tkinter import ttk


# shorten the URL using a call to tinyurl
def shorten_url():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url_ent.get())
    print(short_url_ent.insert(0, short_url))
    time.sleep(1)
    short_url_ent.configure(state='readonly')

# clears the Entry boxes and sets focus back to first Entry box
def clear_entries():
    short_url_ent.configure(state='normal')
    long_url_ent.delete(0, END)
    short_url_ent.delete(0, END)
    long_url_ent.focus()


# creating a root widget (window)
root = Tk()
root.title('URL Shortener')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
root.geometry('300x150')

# create a frame for responsive GUI
frame = Frame(root)

# create & place widgets within a frame
long_url_lbl = ttk.Label(frame, text='Enter Long URL')
long_url_lbl.grid(row=0, column=0, sticky='e')
long_url_ent = ttk.Entry(frame)
long_url_ent.grid(row=0, column=1)

short_url_lbl = ttk.Label(frame, text='Shortened URL')
short_url_lbl.grid(row=1, column=0)
short_url_ent = ttk.Entry(frame)
short_url_ent.grid(row=1, column=1, sticky='e')

short_button = ttk.Button(frame, text='Shorten URL', command=lambda: shorten_url(), width=35)
short_button.grid(row=2, column=0, columnspan=2)

new_button = ttk.Button(frame, text='New URL', command=lambda: clear_entries(), width=35)
new_button.grid(row=3, column=0, columnspan=2)

# for each widget within frame add padding of x=10 and y=5
for widget in frame.winfo_children():
    widget.grid_configure(padx=5, pady=5)

# show frame
frame.pack()

# set focus to first input
long_url_ent.focus()

# create a mainloop to run the root widget
root.mainloop()
