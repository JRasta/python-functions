""" A simple Euro 2024 database
Group Menu Page
Author: J. Smith
Date: 2024
"""

import tkinter
import sqlite3

from tkinter import ttk

class GroupDetails:
    def __init__(self, group):
        if "A" in group:
            group = [('Ger', 'imgs\\team_badges\\ger.png', '0', '0', '0', '0', '0', '0', '0', '0')]
# ('Swi', '0', '0', '0', '0', '0', '0', '0', '0'),
# ('Hun', '0', '0', '0', '0', '0', '0', '0', '0'),
# ('Sco', '0', '0', '0', '0', '0', '0', '0', '0'),]



        # Create main menu
        self.main_menu = tkinter.Tk()
        self.main_menu.title(f"Euro 2024 - Group {group}")

        screen_width = self.main_menu.winfo_screenwidth()
        screen_height = self.main_menu.winfo_screenheight()
        self.main_menu.geometry("600x400+%d+%d" % (screen_width/2-275, screen_height/2-230))

        self.main_menu.iconbitmap("imgs\\football.ico")
        ttk.Style().theme_use('xpnative')

        frame = ttk.Frame(self.main_menu)
        frame.pack()

        screen_label = tkinter.Label(frame, text=f"Group {group}", padx=20, pady=20)
        screen_label.grid(row=0, column=0, columnspan=9)

        country_label = tkinter.Label(frame, text="Country", padx=10)
        country_label.grid(row=1, column=0)
        under_line = tkinter.Label(frame, text="-------")
        under_line.grid(row=2, column=0)

        played_label = tkinter.Label(frame, text="Played", padx=10)
        played_label.grid(row=1, column=1)
        under_line = tkinter.Label(frame, text="-------")
        under_line.grid(row=2, column=1)

        w_label = tkinter.Label(frame, text="W", padx=10)
        w_label.grid(row=1, column=2)
        under_line = tkinter.Label(frame, text="---")
        under_line.grid(row=2, column=2)

        d_label = tkinter.Label(frame, text="D", padx=10)
        d_label.grid(row=1, column=3)
        under_line = tkinter.Label(frame, text="---")
        under_line.grid(row=2, column=3)

        l_label = tkinter.Label(frame, text="L", padx=10)
        l_label.grid(row=1, column=4)
        under_line = tkinter.Label(frame, text="---")
        under_line.grid(row=2, column=4)

        f_label = tkinter.Label(frame, text="F", padx=10)
        f_label.grid(row=1, column=5)
        under_line = tkinter.Label(frame, text="---")
        under_line.grid(row=2, column=5)

        a_label = tkinter.Label(frame, text="A", padx=10)
        a_label.grid(row=1, column=6)
        under_line = tkinter.Label(frame, text="---")
        under_line.grid(row=2, column=6)

        gd_label = tkinter.Label(frame, text="GD", padx=10)
        gd_label.grid(row=1, column=7)
        under_line = tkinter.Label(frame, text="---")
        under_line.grid(row=2, column=7)

        pts_label = tkinter.Label(frame, text="Pts", padx=10)
        pts_label.grid(row=1, column=8)
        under_line = tkinter.Label(frame, text="---")
        under_line.grid(row=2, column=8)

        details_return_btn = tkinter.Button(frame, text="Return", padx=20, pady=20, command=self.main_menu.destroy)
        details_return_btn.grid(row=3, column=0, columnspan=3)

        self.main_menu.mainloop()
