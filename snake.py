import pygame

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

top = 250
left = 250

topDirection = 0
leftDirection = 0

clock = pygame.time.Clock()

#Méthode de mouvement
while not gameOver:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gameOver = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                topDirection = -25
                leftDirection = 0
            elif event.key == pygame.K_RIGHT:
                topDirection = 25
                leftDirection = 0
            elif event.key == pygame.K_UP:
                leftDirection = -25
                topDirection = 0
            elif event.key == pygame.K_DOWN:
                leftDirection = 25
                topDirection = 0

    top += topDirection
    left += leftDirection

    window.fill(green)
    snake = pygame.draw.rect(window, black, [top, left, 25, 25])
    fruit = pygame.draw.rect(window, red, [300, 400, 25, 25])

    pygame.display.update()

    clock.tick(10)

pygame.quit()
quit()
