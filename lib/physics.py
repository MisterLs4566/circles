import pygame
from pygame.locals import *
import sys

pygame.init()

class Physics():
    
    def __init__(self):
        
        super().__init__()
        
        self.g = 9.81

    
    def gravity(self, objects):
        
        for object in objects:
            object.rect.y += 1/2 * self.g * pow(object.seconds, 2)                  


if(__name__ == "__main__"):
   
    sys.exit()