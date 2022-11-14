from tkinter import *
from PIL import ImageTk, Image

# creating a root widget (window)
root = Tk()
root.title('Frame(s)')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon

frame = LabelFrame(root, text='This is my frame...', padx=50, pady=50)
frame.pack(padx=50, pady=50)

button = Button(frame, text='Button in a frame')
button.pack()

# create a mainloop to run the root widget
root.mainloop()
