import sys
import pygame
from pygame.locals import *

pygame.init()

class Sphere(pygame.sprite.Sprite):

    def  __init__(self, system, pos_x, pos_y, scale_x, scale_y):

        super().__init__()
        
        self.system = system

        self.timer = 0
        self.seconds = 0

        self.pos_x = pos_x  
        self.pos_y = pos_y
        self.scale_x = scale_x
        self.scale_y = scale_y

        self.image = pygame.image.load("./sprites/ball.png")
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        
        self.timer += float(1000/self.system.fps)
        self.seconds = float(self.timer/1000)

        self.clear()

    def clear(self):

        if(self.rect.y > self.system.height):

            self.destroy()

    def destroy(self):

        self.system.sprites.remove(self)
        del self

if(__name__ == "__main__"):
    
    sys.exit()