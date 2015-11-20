import pygame
import time
import random
from pygame import *
pygame.init()


display_width = 400
display_height = 500
mousewidth = 75
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dodge')
clock = pygame.time.Clock()

image = pygame.image.load('mouse.png')
def blocks(blockx, blocky, blockw, blockh, color):
    pygame.draw.rect(gameDisplay, color, [blockx, blocky, blockw, blockh])
def mouse(x,y):
    gameDisplay.blit(image, (x,y))
def texts_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

def message_display(text):
    largetext = pygame.font.Font('freesansbold.ttf', 25)
    textsurf, textrect = texts_objects(text, largetext)
    textrect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    time.sleep(2)
    gameloop()
def crash():
    n = time.get_ticks()/1000
    s = str(n)
    string = "You lasted for " + s + " seconds"
    message_display(string)

def gameloop():
    x = (display_width * 0.45)
    y = (display_height * 0.8)



    x_change = 0

    blocks_startx = random.randrange(0, display_width)
    blocks_starty = -600
    blocks_speed = 7
    blocks_width = 100
    blocks_height = 100
    gameExit = False

    while not gameExit:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x_change = -5
                elif event.key == pygame.K_RIGHT:
                    x_change = 5
            if event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    x_change = 0

        x += x_change
        gameDisplay.fill(white)

        blocks(blocks_startx, blocks_starty, blocks_width, blocks_height, black)
        blocks_starty += blocks_speed

        mouse(x,y)

        if x > display_width - mousewidth or x < 0:
            crash()
        if blocks_starty > display_height:
            blocks_starty = 0 - blocks_height
            blocks_startx = random.randrange(0, display_width)

        if y < blocks_starty+blocks_height:

            if x > blocks_startx and x < blocks_startx + blocks_width or x+mousewidth > blocks_startx and x + mousewidth < blocks_startx+blocks_width:

                crash()
        pygame.display.update()
        clock.tick(60)
gameloop()
pygame.quit()
quit()
