# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 19:34:24 2014

@author: pruvolo
"""

import pygame
from pygame.locals import *
import random
import math
import time

class BrickBreakerModel:
    """ Encodes the game state of Brick Breaker """
    def __init__(self):
        self.number_of_lives = 3
        self.bricks = []
        for i in range(640 / 110):
            for j in range(240 / 30):
                new_brick = Brick(10 + 110 * i, 10 + 30 * j, 100, 20, (255, 0, 0))
                self.bricks.append(new_brick)
        print len(self.bricks)

class Brick:
    """ Encodes the state of a brick in Brick Breaker """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color

class PyGameBrickBreakerView:
    """ Renders the BrickBreakerModel to a pygame """
    def __init__(self, model, screen):
        self.model = model
        self.screen = screen

    def draw(self):
        self.screen.fill(pygame.Colir(0, 0, 0))
        for brick in self.model.bricks:
            pygame.draw.rect(
                self.screen,
                pygame.Color(
                    brick.color[0],
                    brick.color[1],
                    brick.color[2]
                ),
                pygame.Rect((self.x, self.y), (self.x + self.width, self.y + self.heigt))
            )
        pygame.display.update()

class Paddle:
    """ Encode the state of the paddle in Brick """
    def __init__(self, x, y, width, height, color):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.color = color
        self.vx =

    def update(self):


def PyGameKeyboardController:
    def __init__(self, model):
        self.model = model

    def handle_pygame_event(self, event):
        if event.type ==

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    mode = BrickBreakerModel()
    view = PyGameBrickBreakerView(model, screen)
    controller = PyGameMouserController(model)

    running = True

    while running:
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        view.draw()
        time.sleep(.001)

    pygame.quit()