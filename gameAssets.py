import pygame
import random

#Fenêtre du jeu
window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake')

#Varioables globales
white = (211, 211, 211)
black = (0, 0, 0)
green = (58, 157, 35)
red = (255, 0, 0)
yellow = (255, 255, 0)
pink = (255, 192, 203)

left = 250
top = 250
leftDirection = 0
topDirection = 0

score = 0

#Fonction pour la couleur du fruit
def fruitColor():
    fruitColor = [red,yellow,pink]
    x = random.randrange(0,3)
    return fruitColor[x]

#Fonction pour dessiner une grille
def grid():
    numberOfColumn = 0
    topLign = 0
    leftLign = 0
    while numberOfColumn < 20:
        pygame.draw.rect(window, white, [leftLign, topLign, 25, 25], 1)
        topLign += 25
        if numberOfColumn < numberOfColumn + 1 and topLign == 500:
            topLign = 0
            leftLign += 25
            numberOfColumn += 1

