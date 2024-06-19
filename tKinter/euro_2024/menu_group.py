""" A simple Euro 2024 database
Group Menu Page
Author: J. Smith
Date: 2024
"""

import tkinter
from tkinter import ttk

import group_details as gp

class GroupMenu:
    @staticmethod
    def group_details(group):
        return gp.GroupDetails(group)

    def __init__(self):
        # Create main menu
        self.main_menu = tkinter.Tk()
        self.main_menu.title("Euro 2024 - Groups")

        screen_width = self.main_menu.winfo_screenwidth()
        screen_height = self.main_menu.winfo_screenheight()
        self.main_menu.geometry("450x400+%d+%d" % (screen_width/2-275, screen_height/2-230))

        self.main_menu.iconbitmap("imgs\\football.ico")
        ttk.Style().theme_use('xpnative')

        frame = ttk.Frame(self.main_menu)
        frame.pack()

        group_title = tkinter.Label(frame, text="Groups", padx=20, pady=20)
        group_title.grid(row=0, column=0, columnspan=3)

        group_a_btn = tkinter.Button(frame, text="Group\nA", padx=35, pady=35, command=lambda: self.group_details("A"))
        group_a_btn.grid(row=1, column=0, padx=10, pady=10)

        group_b_btn = tkinter.Button(frame, text="Group\nB", padx=35, pady=35, command=lambda: self.group_details("B"))
        group_b_btn.grid(row=1, column=1, padx=10, pady=10)

        group_c_btn = tkinter.Button(frame, text="Group\nC", padx=35, pady=35, command=lambda: self.group_details("C"))
        group_c_btn.grid(row=1, column=2, padx=10, pady=10)

        group_d_btn = tkinter.Button(frame, text="Group\nD", padx=35, pady=35, command=lambda: self.group_details("D"))
        group_d_btn.grid(row=2, column=0, padx=10, pady=10)

        group_e_btn = tkinter.Button(frame, text="Group\nE", padx=35, pady=35, command=lambda: self.group_details("E"))
        group_e_btn.grid(row=2, column=1, padx=10, pady=10)

        group_f_btn = tkinter.Button(frame, text="Group\nF", padx=35, pady=35, command=lambda: self.group_details("F"))
        group_f_btn.grid(row=2, column=2, padx=10, pady=10)

        group_return_btn = tkinter.Button(frame, text="Return", padx=20, pady=20, command=self.main_menu.destroy)
        group_return_btn.grid(row=3, column=0, columnspan=3)

        self.main_menu.mainloop()





