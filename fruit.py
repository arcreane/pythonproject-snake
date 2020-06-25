import pygame
from gameAssets import *

class Fruit(object):
    
    def __init__(self):
        self.color = fruitColor()
        self.fruitLeft = random.randrange(0, 500,25)
        self.fruitTop = random.randrange(0, 500,25)
        
    def draw(self, window):
        self.rect = pygame.draw.rect(window, self.color, [self.fruitLeft, self.fruitTop, 25, 25])

    def intersect(self, snake):
        return snake == self.rect
