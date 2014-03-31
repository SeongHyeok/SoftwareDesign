# -*- coding: utf-8 -*-
"""
Created on Mon Mar 31 15:42:09 2014

@author: sim
"""

from abc import ABCMeta, abstractmethod

class Animal(object):
    __metaclass__ = ABCMeta
    @abstractmethod
    def say_something(self):
        pass

class Cat(Animal):
    def say_something(self):
        return "meow!"

class Dog(Animal):
    pass

if __name__ == '__main__':
    c = Cat()
    d = Dog()