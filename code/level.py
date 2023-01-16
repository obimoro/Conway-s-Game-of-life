import pygame as pg
import numpy as np

from settings import *

class Level:
    def __init__(self, screen):
        self.screen = screen
        # create a array in a certain size with the vaule 0 or 1
        self.map = np.random.randint(2, size=(ARR_H,ARR_W))

    def update(self):
        self.map = np.random.randint(2, size=(ARR_H,ARR_W))
        return self.map

    def display(self):
        # Creates a copy of previous array with its content
        self.next_map = self.map.copy()

        for x in range(ARR_W - 1):
            for y in range(ARR_H - 1):

                num = 0
                #if self.next_map[x - 1][y - 1] == 1:
                #    num += 1
                #if self.next_map[x][y - 1] == 1:
                #    num += 1
                #if self.next_map[x + 1][y - 1] == 1:
                #    num += 1
                #if self.next_map[x - 1][y] == 1:
                #    num += 1
                #if self.next_map[x + 1][y] == 1:
                #    num += 1
                #if self.next_map[x - 1][y + 1] == 1:
                #    num += 1
                #if self.next_map[x][y + 1] == 1:
                #    num += 1
                #if self.next_map[x + 1][y + 1] == 1:
                #    num += 1
                if self.next_map[y - 1][x - 1] == 1:
                    num += 1
                if self.next_map[y][x - 1] == 1:
                    num += 1
                if self.next_map[y + 1][x - 1] == 1:
                    num += 1
                if self.next_map[y - 1][x] == 1:
                    num += 1
                if self.next_map[y + 1][x] == 1:
                    num += 1
                if self.next_map[y - 1][x + 1] == 1:
                    num += 1
                if self.next_map[y][x + 1] == 1:
                    num += 1
                if self.next_map[y + 1][x + 1] == 1:
                    num += 1

                
                if self.next_map[x][y] == 1 and (num == 2 or num == 3):
                    self.next_map[x][y] = 1
                elif self.next_map[x][y] == 0 and num == 3:
                    self.next_map[x][y] = 1
                else:
                    self.next_map[x][y] = 0    
                print(num)
                self.map = self.next_map
        return self.map

    def render(self):
        # Goes throught each element and draws a Rect, 0 (dead = white), 1 (alive = black)
        for row_index, rows in enumerate(self.map):
            for col_index, cols in enumerate(rows):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if cols == 0:
                    pg.draw.rect(self.screen, (255,255,255), (x, y, TILESIZE - TILE_OFFSET,TILESIZE - TILE_OFFSET))
                elif cols == 1:
                    pg.draw.rect(self.screen, (0,0,0),  (x,y, TILESIZE - TILE_OFFSET,TILESIZE - TILE_OFFSET))

        self.display()