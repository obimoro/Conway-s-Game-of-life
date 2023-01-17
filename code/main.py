import pygame as pg
import numpy as np
import sys

from settings import *
from level import *

class App:
    def __init__(self):
        # initialize pygame
        pg.init()
        # setting up pygame screen
        self.screen = pg.display.set_mode((SCR_WIDTH,SCR_HEIGHT))
        self.level = Level(self.screen)
        # Timing
        self.clock = pg.time.Clock()

        
    # event handler og pygame
    def check_event(self):
        for event in pg.event.get():
            # checks if window is being closed and then exits gracefully 
            if event.type == pg.QUIT  or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()
            # Restarts the grid
            if event.type == pg.KEYDOWN and event.key == pg.K_r:
                self.level.resetLevel()

                
    # render to the screen
    def render(self):
        # fills the windows with color (orange) and then,
        # updates the screen
        self.screen.fill((128,128,128))
        self.level.render()
        pg.display.flip()
        #pg.draw.rect(self.screen, (0,0,0), (200,150,100,50))

    # Applications run loop
    def run(self):
        while True:
            self.check_event()
            self.render()
            self.clock.tick(60)

# checks if current file is correct and creates an object of the 
# application class, then runs
if __name__ == '__main__':
    game = App()
    game.run()