import pygame
import window

print("Welcome to Snake")
black = (0,0,0)
window.window()
gameOver = False
top = 250
left = 250
clock = pygame.time.Clock()
while not gameOver :
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left -=25
            elif event.key == pygame.K_RIGHT:
                left +=25
            elif event.key == pygame.K_UP:
                top -=25
            elif event.key == pygame.K_DOWN:
                top +=25
    pygame.draw.rect(window.window().window, black, [left,top, 25,25])
    pygame.display.update()
