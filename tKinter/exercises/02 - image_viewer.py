""" A simple image viewer
Author: FreeCodeAcademy
Date: 2022
"""

from tkinter import *
from PIL import ImageTk, Image

# creating a root widget (window)
root = Tk()
root.title('Icons, Images, Exit Button(s)')
root.iconbitmap('..\\misc\\tech.ico')  # add user defined icon

def forward(img_num):
    global img_lbl
    global button_forward
    global button_back

    img_lbl.grid_forget()  # forget what is being displayed
    img_lbl = Label(image=image_list[img_num - 1])  # display new image
    button_forward = Button(root, text='>>', command=lambda: forward(img_num + 1))  # move forward
    button_back = Button(root, text='<<', command=lambda: back(img_num - 1))  # move back

    # if final image disabled forward button
    if img_num == 4:
        button_forward = Button(root, text='>>', state=DISABLED)

    # add the new image and forward and back buttons
    img_lbl.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0, pady=50, padx=20)
    button_forward.grid(row=1, column=2, pady=50, padx=20)

    # status bar
    status = Label(root, text='Image ' + str(img_num) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


def back(img_num):
    global img_lbl
    global button_forward
    global button_back

    img_lbl.grid_forget()  # forget what is being displayed
    img_lbl = Label(image=image_list[img_num - 1])  # display new image
    button_forward = Button(root, text='>>', command=lambda: forward(img_num + 1))  # move forward
    button_back = Button(root, text='<<', command=lambda: back(img_num - 1))  # move back

    # if first image disabled back button
    if img_num == 1:
        button_back = Button(root, text='<<', state=DISABLED)

    # add the new image and forward and back buttons
    img_lbl.grid(row=0, column=0, columnspan=3)
    button_back.grid(row=1, column=0, pady=50, padx=20)
    button_forward.grid(row=1, column=2, pady=50, padx=20)

    # status bar
    status = Label(root, text='Image ' + str(img_num) + ' of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
    status.grid(row=2, column=0, columnspan=3, sticky=W + E)


# insert images
img_1 = ImageTk.PhotoImage(Image.open('..\\misc\\afghanistan.png'))
img_2 = ImageTk.PhotoImage(Image.open('..\\misc\\aland.png'))
img_3 = ImageTk.PhotoImage(Image.open('..\\misc\\algeria.png'))
img_4 = ImageTk.PhotoImage(Image.open('..\\misc\\angola.png'))

# create a list for the images
image_list = [img_1, img_2, img_3, img_4]

# starting image
img_lbl = Label(image=img_1)
img_lbl.grid(row=0, column=0, columnspan=3)

# buttons
button_back = Button(root, text='<<', command=back, state=DISABLED)
button_exit = Button(root, text='Exit Program', command=root.quit)
button_forward = Button(root, text='>>', command=lambda: forward(2))

button_back.grid(row=1, column=0, pady=50, padx=20)
button_exit.grid(row=1, column=1, pady=50, padx=20)
button_forward.grid(row=1, column=2, pady=10, padx=20)

status = Label(root, text='Image 1 of ' + str(len(image_list)), bd=1, relief=SUNKEN, anchor=E)
status.grid(row=2, column=0, columnspan=3, sticky=W+E)

# create a mainloop to run the root widget
root.mainloop()
