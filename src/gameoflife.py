import pygame

class Cell:
    def __init__(self, neighbours, x, y):
        self.alive = False
        self.neighbours = neighbours
        self.x = x
        self.y = y
