import pygame
import time
import random
from pygame import *
from random import randint
pygame.init()

#### Game Settings #######################
display_width = 400
display_height = 500
mousewidth = 75
#image = pygame.image.load('mouse.png')

#### color options #######################
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

#### Inititalize Object Parameters  #################################
init_x = random.randrange(0, display_width)
init_y = -600
init_vel = randint(10,16)
init_w = 100
init_h = 100

pygame.display.set_caption('Dodge')

class State():
    gameExit = False
    gameDisplay = pygame.display.set_mode((display_width, display_height))

    def blocks(self, color=black):
        pygame.draw.rect(gameDisplay, color, [block_x, block_y, block_w, blockh])

    def __init__(self):
        self.image = pygame.image.load('mouse.png')
        self.gameDisplay = pygame.display.set_mode((display_width, display_height))
        self.clock = pygame.time.Clock()
        self.block_x = init_x
        self.block_y = init_y
        self.block_w = init_w
        self.block_h = init_h

game = State()

print(game)


class Player(State):
    def mouse(x,y):
        gameDisplay.blit(image, (x,y))

    def texts_objects(text, font):
        textsurface = font.render(text, True, black)
        return textsurface, textsurface.get_rect()

    def message_display(text, ct):
        largetext = pygame.font.Font('freesansbold.ttf', 25)
        textsurf, textrect = texts_objects(text, largetext)
        textrect.center = ((display_width/2), (display_height/2))
        gameDisplay.blit(textsurf, textrect)
        pygame.display.update()
        pygame.time.wait(2000)
        gameloop(ct+2000);


# text display settings


# when game ends displays how long the player survived
def crash(ct):
    n = (time.get_ticks() - ct)/1000
    s = str(n)
    ct = time.get_ticks();
    string = "You lasted for " + s + " seconds"
    message_display(string, ct)

# main game loop, updates objects on screen and detects collision
def gameloop(ct):
    x = (display_width * 0.45)
    y = (display_height * 0.8)
    x_change = 0



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
            crash(ct)

        if blocks_starty > display_height:
            blocks_starty = 0 - blocks_height
            blocks_startx = random.randrange(0, display_width)

        if y < blocks_starty+blocks_height:
             if x > blocks_startx and x < blocks_startx + blocks_width or x+mousewidth > blocks_startx and x + mousewidth < blocks_startx+blocks_width:
                crash(ct)

        pygame.display.update()
        clock.tick(60)
gameloop(0)
pygame.quit()
quit()
