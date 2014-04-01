# -*- coding: utf-8 -*-
"""
Created on Wed Apr 21 23:07:27 2014

@author: pruvolo
"""

import pygame
from pygame.locals import *
import time

from abc import ABCMeta, abstractmethod

class Drawable(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def draw(self):
        pass

class AnimatedDrawable(object):
    def __init__(self, drawble, v_x, v_y):
        self.drawable = drawable
        self.v_x = v_x
        self.v_y = v_y

    @abstractmethod
    def draw(self, screen):
        self.drawable.draw(screen)

    @abstractmethod
    def translate(self):
        self.drawable.translate()

class Circle(Drawable):
    """ Reperesents a cirlce that can draw itself to a pygame window. """
    def __init__(self,center_x,center_y,radius):
        """ Initialize the Circle object.

            center_x: the x-coordinate of the center of the circle
            center_y: the y-coordinate of the center of the circle
            radius: the radius of the circle
        """
        self.center_x = center_x
        self.center_y = center_y
        self.radius = radius

    def draw(self,screen):
        """ Draw the Circle to the screen.

            screen: the pygame screen to draw to
        """
        pygame.draw.circle(screen, pygame.Color(0,0,0), (self.center_x,self.center_y),self.radius,1)

    def translate(self, delta_x, delta_y):
        self.center_x += delta_x
        self.center_y += delta_y

class Polygon(Drawable):
    """ Represents a polygon that can draw itself to a pygame window. """
    def __init__(self,vertices):
        """ Initialize a Polygon object.

            vertices: the vertices of the polygon represented as a list of
                      two elemenet lists that represent (x,y) coordinates
                      of the polygon's vertices.
        """
        self.vertices = vertices

    def draw(self,screen):
        """ Draw the the Polygon to the screen.

            screen: the pygame screen to draw to
        """
        for i in range(len(self.vertices)):
            j = (i+1)%len(self.vertices)
            pygame.draw.line(screen,pygame.Color(0,0,0),(self.vertices[i][0],self.vertices[i][1]),(self.vertices[j][0], self.vertices[j][1]))

    def translate(self, delta_x, delta_y):
        for v in self.vertices:
            v[0] += delta_x
            v[1] += delta_y

class Quadrilateral(Polygon):
    """ Represents a quadrilateral that can draw itself to a pygame window """
    def __init__(self,x1,y1,x2,y2,x3,y3,x4,y4):
        """ Initialize a Quadrilateral object.

            x1: x-coordinate of the first vertex of the quadrilateral
            y1: y-coordinate of the first vertex of the quadrilateral
            x2: x-coordinate of the second vertex of the quadrilateral
            y2: y-coordinate of the second vertex of the quadrilateral
            x3: x-coordinate of the third vertex of the quadrilateral
            y3: y-coordinate of the third vertex of the quadrilateral
            x4: x-coordinate of the fourth vertex of the quadrilateral
            y4: y-coordinate of the fourth vertex of the quadrilateral
        """
        super(Quadrilateral,self).__init__([[x1,y1],[x2,y2],[x3,y3],[x4,y4]])

class Rectangle(Quadrilateral):
    """ Represents a rectangle that can draw itself to a pygame window. """

    def __init__(self, x_ul, y_ul, width, height):
        """ Initialize a Rectangle object.

            x_ul: x-coordinate of upper-left corner
            y_ul: y-coordinate of upper-left corner
            width: width of the rectangle
            height: height of the rectangle
        """
        super(Rectangle, self).__init__(x_ul, y_ul, x_ul+width, y_ul, x_ul+width, y_ul+height, x_ul, y_ul+height)

class Square(Rectangle):
    """ Represents asquare that can draw itself to a pygame window. """
    def __init__(self,x_ul,y_ul,side_length):
        """ Initialize a Square object.

            x_ul: the x-coordinate of the upper left corner of the square
            y_ul: the y-coordinate of the upper left corner of the square
            side_length: the side length of the square.
        """
        super(Square, self).__init__(x_ul,y_ul,side_length,side_length)

if __name__ == '__main__':
    pygame.init()

    size = (640,480)
    screen = pygame.display.set_mode(size)

    """quad = Quadrilateral(100,100,200,90,200,300,100,300)
    rect = Rectangle(250,250,100,40)
    square = Square(400,400,20)
    triangle = Polygon([[300,300],[350,250],[400,300]])
    circle = Circle(400,100,40)"""
    shapes = []
    shapes.append(Quadrilateral(100,100,200,90,200,300,100,300))
    shapes.append(Rectangle(250,250,100,40))
    shapes.append(Square(400,400,20))
    shapes.append(Polygon([[300,300],[350,250],[400,300]]))
    shapes.append(Circle(400,100,40))
    running = True

    while running:
        screen.fill(pygame.Color(255,255,255))
        """quad.draw(screen)
        rect.draw(screen)
        square.draw(screen)
        triangle.draw(screen)
        circle.draw(screen)"""
        for shape in shapes:
            if isinstance(shape, Drawable):
                shape.draw(screen)
            else:
                print "Error: object is not drawable."
        for event in pygame.event.get():
            if event.type == QUIT:
                running = False
        time.sleep(.01)
        pygame.display.update()

    pygame.quit()