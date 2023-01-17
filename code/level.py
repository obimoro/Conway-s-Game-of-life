import pygame as pg
import numpy as np

from settings import *

class Level:
    def __init__(self, screen):
        self.screen = screen
        # create a array in a certain size with the vaule 0 or 1
        self.map = np.random.randint(2, size=(ROWS,COLUMNS))

    def resetLevel(self):
        self.map = np.random.randint(2, size=(ROWS,COLUMNS))
        return self.map


    def render(self):
        # Goes throught each element and draws a Rect, 0 (dead = white), 1 (alive = black)
        for x in range(ROWS):
            for y in range(COLUMNS):
                x_pos = x * TILESIZE
                y_pos = y * TILESIZE
                if self.map[x][y] == 1:
                    pg.draw.rect(self.screen, (0,0,0), (x_pos, y_pos, TILESIZE -1, TILESIZE -1))
                else:
                    pg.draw.rect(self.screen, (255,255,255), (x_pos, y_pos, TILESIZE -1, TILESIZE -1))

        # Uses the neighbors function and then applies the rules of
        # Conways game of life and updates the tile with either 
        # dead or alive (0 or 1)
        for x in range(ROWS):
            for y in range(COLUMNS):
                neighbors = self.neighbors(x, y)
                state = self.map[x][y]       
                if state == 0 and neighbors == 3:
                    self.map[x][y] = 1
                elif state == 1 and (neighbors < 2 or neighbors > 3):
                    self.map[x][y] = 0
                else:
                    self.map[x][y] = state

    # Checks all the neighbor around x and y, with a wrap around the grid using modilo
    # then returns the added sum of neighbors
    def neighbors(self, x ,y):     
        sum = 0
        for i in range(-1, 2):
            for j in range(-1 ,2):
                col = (x + i + COLUMNS) % COLUMNS
                row = (y + j + ROWS) % ROWS
                sum += self.map[row][col]
        sum -= self.map[x][y]
        return sum