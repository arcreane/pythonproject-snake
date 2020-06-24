import pygame

green = (58, 157, 35)
white = (211,211,211)

class window():
    # Taille de la fenetre 500px*500px
    window = pygame.display.set_mode((500, 500))

    #Nom de la fenetre de jeu
    pygame.display.set_caption("Snake")

    #Background color de la fenetre
    window.fill(green)

    #Grille
    numberOfColumn = 0
    top = 0
    left = 0
    while numberOfColumn < 20 :
        pygame.draw.rect(window, white, [left,top, 25,25], 1)
        top += 25
        if numberOfColumn < numberOfColumn + 1 and top == 500:
            top = 0
            left +=25
            numberOfColumn += 1
        pygame.display.update()
    
    
