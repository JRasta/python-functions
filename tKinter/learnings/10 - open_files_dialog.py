from tkinter import *
from PIL import ImageTk, Image
from tkinter import filedialog

img = ''

# creating a root widget (window)
root = Tk()
root.title('Open File Dialog')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon

def openfile():
    global img
    # open directory to show pictures
    root.filename = filedialog.askopenfilename(initialdir='..\\misc', title='Open file',
                                               filetypes=(('png files', '*.png'), ('all files', '*.*')))
    # get the path of selected picture
    Label(root, text=root.filename).pack()

    # add selected img to main window
    img = ImageTk.PhotoImage(Image.open(root.filename))
    Label(image=img).pack()


# open file dialog
btn = Button(root, text='Open File', command=openfile)
btn.pack()

# create a mainloop to run the root widget
root.mainloop()
