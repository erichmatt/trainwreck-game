import pygame
import random
from time import sleep
from pygame.locals import *
import sys

pygame.init()

white = (255,255,255)
black = (0,0,0)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0,0, 255)
gray = (100, 100, 100)

    
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption('TRAIN WRECK')

def draw_train(surf, pos):
    train = pygame.image.load('pixel-train2.png')
    screen.blit(train,pos)

screen.fill(green)

x = (300)
y = (300)
class Train(object):
    def __init__(self):
        self.position = (0,0)
        self.randomize()
    def randomize(self):
        self.position = (random.randint(0,300),random.randint(0,300))
    def position(self,x,y):
        self.postion = (x,y)
    def draw(self, surf):
        draw_train(surf,self.position)

train = Train()
train2 = Train()
train2.draw(screen)
print train.position
train.position = (train.position[0]+10,train.position[1])
train.draw(screen)
print train.position
pygame.display.flip()
pygame.display.update()
