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
image = pygame.image.load('mouse.png')

#### color options #######################
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

#### Initialize Pygame #################################
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dodge')
clock = pygame.time.Clock()

class Player():
    def __init__(self):
        self.x = (display_width * 0.45)
        self.y = (display_height * 0.8)

    def mouse(self):
        gameDisplay.blit(image, (self.x, self.y))

class Blocks():
    def __init__(self):
        self.blocks_startx = random.randrange(0, display_width)
        self.blocks_starty = -600
        self.blocks_speed = randint(10,16)
        self.blocks_width = 100
        self.blocks_height = 100

def blocks(blocks_startx, blocks_starty, blocks_width, blocks_height, color):
    pygame.draw.rect(gameDisplay, color, [blocks_startx, blocks_starty, blocks_width, blocks_height])

def texts_objects(text, font):
    textsurface = font.render(text, True, black)
    return textsurface, textsurface.get_rect()

# text display settings
def message_display(text, ct):
    largetext = pygame.font.Font('freesansbold.ttf', 25)
    textsurf, textrect = texts_objects(text, largetext)
    textrect.center = ((display_width/2), (display_height/2))
    gameDisplay.blit(textsurf, textrect)
    pygame.display.update()
    pygame.time.wait(2000)
    gameloop(ct+2000);

# when game ends displays how long the player survived
def crash(ct):
    n = (time.get_ticks() - ct)/1000
    s = str(n)
    ct = time.get_ticks();
    string = "You lasted for " + s + " seconds"
    message_display(string, ct)

# main game loop, updates objects on screen and detects collision
def gameloop(ct):
    x_change = 0
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

        player.x += x_change
        gameDisplay.fill(white)

        blocks(block.blocks_startx, block.blocks_starty, block.blocks_width, block.blocks_height,black)
        block.blocks_starty += block.blocks_speed

        player.mouse()

        if player.x > display_width - mousewidth or player.x < 0:
            crash(ct)

        if block.blocks_starty > display_height:
            block.blocks_starty = 0 - block.blocks_height
            block.blocks_startx = random.randrange(0, display_width)

        if player.y < block.blocks_starty+block.blocks_height:
             if player.x > block.blocks_startx and player.x < block.blocks_startx + block.blocks_width or player.x+mousewidth > block.blocks_startx and player.x + mousewidth < block.blocks_startx+ block.blocks_width:
                crash(ct)

        pygame.display.update()
        clock.tick(60)
player = Player()
block = Blocks()
gameloop(0)
pygame.quit()
quit()
