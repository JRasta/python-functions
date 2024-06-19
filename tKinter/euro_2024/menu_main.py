""" A simple Euro 2024 database
Main Menu Page
Author: J. Smith
Date: 2024
"""
import sqlite3
import tkinter
from tkinter import ttk

import menu_group as mg
import generate_db as db

# Create main menu
main_menu = tkinter.Tk()
main_menu.title("Euro 2024 - Information Desk")

screen_width = main_menu.winfo_screenwidth()
screen_height = main_menu.winfo_screenheight()
main_menu.geometry("400x400+%d+%d" % (screen_width/2-275, screen_height/2-230))

main_menu.iconbitmap("imgs\\football.ico")
ttk.Style().theme_use('xpnative')

db.DB()

def group_window():
    return mg.GroupMenu()

def team_window():
    team_win = tkinter.Tk()
    team_win.title("Euro 2024 - Teams")
    team_win.geometry("500x500")
    team_win.iconbitmap("imgs\\football.ico")
    ttk.Style().theme_use('xpnative')

    team_frame = ttk.Frame(team_win)
    team_frame.pack()

    group_title = tkinter.Label(team_frame, text="Team List")
    group_title.grid(row=0, column=0)


def top_scorer_window():
    top_scorer_win = tkinter.Tk()
    top_scorer_win.title("Euro 2024 - Top Scorer in Each team")
    top_scorer_win.geometry("500x500")
    top_scorer_win.iconbitmap("imgs\\football.ico")
    ttk.Style().theme_use('xpnative')

    top_scorer_frame = ttk.Frame(top_scorer_win)
    top_scorer_frame.pack()

    group_title = tkinter.Label(top_scorer_frame, text="Team List")
    group_title.grid(row=0, column=0)


# Create frame
frame = ttk.Frame(main_menu)
frame.pack()

main_menu_group_btn = tkinter.Button(frame, text="Group\nStages", padx=33, pady=33, command=group_window)
main_menu_group_btn.grid(row=0, column=0)

main_menu_team_btn = tkinter.Button(frame, text="\nTeams", padx=35, pady=35, command=team_window)
main_menu_team_btn.grid(row=0, column=1)

main_menu_top_scorer_btn = tkinter.Button(frame, text="Top\nScorer", padx=35, pady=35, command=top_scorer_window)
main_menu_top_scorer_btn.grid(row=1, column=0, padx=10, pady=10)

main_menu_fixtures_btn = tkinter.Button(frame, text="\nFixtures", padx=35, pady=35)
main_menu_fixtures_btn.grid(row=1, column=1)

main_menu_results_btn = tkinter.Button(frame, text="\nResults", padx=35, pady=35)
main_menu_results_btn.grid(row=2, column=0, padx=10, pady=10)

main_menu_quit_btn = tkinter.Button(frame, text="\nQuit", padx=35, pady=35, command=main_menu.destroy)
main_menu_quit_btn.grid(row=2, column=1, padx=10, pady=10)

main_menu.mainloop()
