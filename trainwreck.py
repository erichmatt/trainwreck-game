import pygame
from time import sleep
from pygame.locals import *
import sys
usrin = raw_input("Press Key: ")


pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0, 255)
gray = (100, 100, 100)
 

train = pygame.image.load('pixel-train2.png')
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('TRAIN WRECK')

screen.fill(green)

x = (300)
y = (300)


if usrin == "w":

    for x in range(500):
        x == x + 20
        screen.blit(train,(x,y))
        pygame.display.flip()
        sleep(0.01)
