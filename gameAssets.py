import random

white = (211, 211, 211)
black = (0, 0, 0)
green = (58, 157, 35)
red = (255, 0, 0)
yellow = (255, 255, 0)
pink = (255, 192, 203)

def fruitColor():
    fruitColor = [red,yellow,pink]
    x = random.randrange(0,3)
    return fruitColor[x]
