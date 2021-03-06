import pygame
import random
import time
from fruit import *
from gameAssets import *

pygame.init()

myGrid = grid()
myColor = fruitColor()

fruit = Fruit()
                    
gameOver = False

clock = pygame.time.Clock()

window.fill(green)
grid()

class Snake(object):
    
    while not gameOver:
        window.fill(green)
        grid()
        
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

        snake = pygame.draw.rect(window, black, [left, top, 25, 25])
        fruit.draw(window)
        
        if fruit.intersect(snake):
            fruitLeft = random.randrange(0, 500,25)
            fruitTop = random.randrange(0, 500,25)
            myColor = fruitColor()
            fruit = Fruit()
            pygame.display.update()
            score +=10

        if snake.left > 500 or snake.top > 500 or snake.width < 0 or snake.height < 0 :
            scoreMessage = "Votre score : %d" % score
            font = pygame.font.Font(None, 50)
            gameOverMessage = font.render('Game Over', True, red, white)
            displayScoreMessage = font.render(scoreMessage, True, red, white)
            window.blit(gameOverMessage, (150, 225))
            window.blit(displayScoreMessage, (150, 275))
            gameOver = True

        pygame.display.update()
        
        clock.tick(10)
    
pygame.quit()
quit()
