from tkinter import *
import pyshorteners

def shorten():
    shortener = pyshorteners.Shortener()
    short_url = shortener.tinyurl.short(long_url_ent.get())
    print(short_url_ent.insert(0, short_url))


# creating a root widget (window)
root = Tk()
root.title('URL Shortener')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon
root.geometry('300x150')

# create widgets
long_url_lbl = Label(root, text='Enter Long URL')
long_url_ent = Entry(root)
short_url_lbl = Label(root, text='Output Shorten URL')
short_url_ent = Entry(root)
short_button = Button(root, text='Shorten URL', command=lambda: shorten())

# place widgets in root widget
long_url_lbl.pack()
long_url_ent.pack()
short_url_lbl.pack()
short_url_ent.pack()
short_button.pack()

# create a mainloop to run the root widget
root.mainloop()
