import pygame
import random

pygame.init()

print("Welcome to Snake")

white = (211, 211, 211)
black = (0, 0, 0)
green = (58, 157, 35)
red = (255, 0, 0)

window = pygame.display.set_mode((500, 500))
pygame.display.set_caption('Snake')

#Affichage d'une grille sur la fenêtre
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
        pygame.display.update()

gameOver = False

left = 250
top = 250

leftDirection = 0
topDirection = 0

fruitLeft = random.randrange(0, 500,25)
fruitTop = random.randrange(0, 500,25)

score = 0

clock = pygame.time.Clock()

#Méthode de mouvement
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                leftDirection = -25
                topDirection = 0
            elif event.key == pygame.K_RIGHT:
                leftDirection = 25
                topDirection = 0
            elif event.key == pygame.K_UP:
                topDirection = -25
                leftDirection = 0
            elif event.key == pygame.K_DOWN:
                topDirection = 25
                leftDirection = 0
        

    left += leftDirection
    top += topDirection

    window.fill(green)
    snake = pygame.draw.rect(window, black, [left, top, 25, 25])
    fruit = pygame.draw.rect(window, red, [fruitLeft, fruitTop, 25, 25])

    if snake == fruit:
        fruitLeft = random.randrange(0, 500,25)
        fruitTop = random.randrange(0, 500,25)
        fruit = pygame.draw.rect(window, red, [fruitLeft, fruitTop, 25, 25])
        pygame.display.update()
        score +=1
        print(score)

    pygame.display.update()

    clock.tick(10)

pygame.quit()
quit()
