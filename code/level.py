import pygame as pg
import numpy as np

from settings import *

class Level:
    def __init__(self, screen):
        self.screen = screen
        # create a array in a certain size with the vaule 0 or 1
        self.map = np.random.randint(2, size=(16,16))


    def display(self):
        # Goes throught each element and draws a Rect, 0 (dead = white), 1 (alive = black)
        for row_index, rows in enumerate(self.map):
            for col_index, cols in enumerate(rows):
                x = col_index * TILESIZE
                y = row_index * TILESIZE
                if cols == 0:
                    pg.draw.rect(self.screen, (255,255,255), (x, y, TILESIZE - TILE_OFFSET,TILESIZE - TILE_OFFSET))
                elif cols == 1:
                    pg.draw.rect(self.screen, (0,0,0),  (x,y, TILESIZE - TILE_OFFSET,TILESIZE - TILE_OFFSET))
        
        # Creates a copy of previous array with its content
        self.next_map = self.map.copy()

        for row_index, rows in enumerate(self.next_map):
            for col_index, cols in enumerate(rows):
                x = col_index
                y = row_index
                 

                 #Go through neighbours
                neighboursAlive = 0
                neighboursAlive += self.next_map[4][4]
                neighboursAlive += self.next_map[4][4 - 1]
                neighboursAlive += self.next_map[4 - 1][4]
                print(neighboursAlive)
                if neighboursAlive >= 2:
                    self.next_map[4][4] = 1
                elif neighboursAlive <= 2:
                    self.next_map[4][4] = 0
                self.map = self.next_map
