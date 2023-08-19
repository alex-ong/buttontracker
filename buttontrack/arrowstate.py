"""
Class to keep button state
"""
import pygame

import os

# Set this to 1 to enable joystick working in background.
os.environ["SDL_JOYSTICK_ALLOW_BACKGROUND_EVENTS"] = "1"

LEFT = 0
DOWN = 1
UP = 2
RIGHT = 3


class ArrowState:
    """Class that keeps track of how many arrows you've pressed"""

    def __init__(self):
        self.up = True
        self.down = True
        self.left = True
        self.right = True
        self._buttons_pressed = 0

    @property
    def buttons_pressed(self):
        """returns how many buttons you pressed"""
        return self._buttons_pressed

    def update(self, event):
        """pleb code instead of a nice map..."""
        if event.type == pygame.JOYBUTTONDOWN:
            if event.button == LEFT:
                self.left = True
            elif event.button == DOWN:
                self.down = True
            elif event.button == RIGHT:
                self.right = True
            elif event.button == UP:
                self.up = True
            else:
                return
            self._buttons_pressed += 1
        elif event.type == pygame.JOYBUTTONUP:
            if event.button == LEFT:
                self.left = False
            elif event.button == DOWN:
                self.down = False
            elif event.button == RIGHT:
                self.right = False
            elif event.button == UP:
                self.up = False
        elif event.type == pygame.KEYDOWN:
            if event.key == 97:  # a
                self.left = True
            elif event.key == 115:  # s
                self.down = True
            elif event.key == 100:  # d
                self.right = True
            elif event.key == 119:  # f
                self.up = True
            else:
                return  # don't add one to count
            self._buttons_pressed += 1

        elif event.type == pygame.KEYUP:
            if event.key == 97:  # a
                self.left = False
            elif event.key == 115:  # s
                self.down = False
            elif event.key == 100:  # d
                self.right = False
            elif event.key == 119:  # f
                self.up = False
