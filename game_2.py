import pygame
from random import randint

############## Display Size #############################
display_width = 1000
display_height = 800

############## Initialize Pygame ########################
pygame.init()
gameDisplay = pygame.display.set_mode((display_width, display_height))
pygame.display.set_caption('Dodge')
clock = pygame.time.Clock()

############## Color options ############################
black = (0,0,0)
white = (255,255,255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0,255)

############## Load images ##############################
myimage = pygame.image.load("cat.bmp")
image = pygame.image.load('stickfig.png')

############## Initialize variables #####################
currentStateX = [randint(0,display_width)]
currentStateY = [0]
currentStateVel = [1]
x_change = 0
x = (display_width * 0.45)
y = (display_height * 0.8)

############## Game Options ##############################
maxObjects = 10 # maximum number of objects on the screen at a given time
objectChance = .01*100 # chance of spawning a new object



def updateDisplay(currentStateX, currentStateY, currentStateVel,x ,y ):
    gameDisplay.fill(black)
    gameDisplay.blit(image, (x,y))

    for i in range(0,len(currentStateX)):
        gameDisplay.blit(myimage,(currentStateX[i],currentStateY[i]))

def updateState(currentStateX, currentStateY, currentStateVel, x, y):
    for i in range(0,len(currentStateX)-1):
        currentStateY[i] += currentStateVel[i] #randint(1,2)
        if currentStateY[i] > (display_height - 100):
            del currentStateX[i]
            del currentStateY[i]
            del currentStateVel[i]

    if randint(0,100) <= objectChance:
        currentStateX.append(randint(0,display_width))
        currentStateY.append(0)
        currentStateVel.append(randint(1,5))

    x += x_change
    return(currentStateX, currentStateY, currentStateVel)


collide = False

while not collide:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            collide = True
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
    #update(x,y)
    updateDisplay(currentStateX, currentStateY, currentStateVel, x, y)
    updateState(currentStateX, currentStateY, currentStateVel, x, y)
    pygame.display.update()
    clock.tick(60)
pygame.quit()
quit()
