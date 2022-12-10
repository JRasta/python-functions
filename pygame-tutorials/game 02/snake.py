# Snake Python Tutorial with Objects and Classes

import math
import random
import pygame
import tkinter as tk
from tkinter import messagebox

width = 0
rows = 0

class Cube(object):  # Class names should use CamelCase convention
    rows = 0
    w = 0

    def __init__(self, start, dirnx=1, dirny=0, color=(255, 0, 0)):
        pass

    def move(self, dirnx, dirny):
        pass

    def draw(self, surface, eyes=False):
        pass

class Snake(object):
    body = []
    turns = {}

    def __init__(self, color, pos):
        self.color = color
        self.head = Cube(pos)
        self.body.append(self.head)

    def move(self):
        pass

    def reset(self):
        pass

    def add_cube(self):
        pass

    def draw(self):
        pass

def draw_grid(w, r, surface):
    size_btwn = w // r
    x = 0
    y = 0

    for i in range(rows):
        x = x + size_btwn
        y = y + size_btwn

        pygame.draw.line(surface, (255, 255, 255), (x, 0), (x, w))  # draw line vertically
        pygame.draw.line(surface, (255, 255, 255), (0, y), (w, y))  # draw line horizontally

def re_draw_window(surface):
    global rows, width
    surface.fill((0, 0, 0))
    draw_grid(width, rows, surface)
    pygame.display.update()

def random_snack(r, items):
    pass

def message_box(subject, content):
    pass

def main():
    global width, rows
    width = 500
    rows = 20
    win = pygame.display.set_mode((width, width))

    # create a snake object
    s = Snake((255, 0, 0), (10, 10))

    # clock object
    clock = pygame.time.Clock()

    # main program
    flag = True
    while flag:
        pygame.time.delay(50)  # delay by 0.5 | 50 milliseconds => lower = faster
        clock.tick(10)  # runs at 10 fps => lower = slower
        re_draw_window(win)  # re-draw window


main()
