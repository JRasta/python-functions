from tkinter import *
from PIL import ImageTk, Image

# creating a root widget (window)
root = Tk()
root.title('Icons, Images, Exit Button(s)')

# add user defined icon
root.iconbitmap('..\\misc\\tech.ico')

# insert images
img = ImageTk.PhotoImage(Image.open('..\\misc\\yt.png'))
img_lbl = Label(image=img, bg='white')
img_lbl.pack()

# end program - programmatically
button_exit = Button(root, text='Exit', command=root.quit)
button_exit.pack()

# create a mainloop to run the root widget
root.mainloop()
