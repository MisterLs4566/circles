import pygame
from pygame.locals import *
import sys

pygame.init()

class Physics():
    
    def __init__(self, system):
        
        super().__init__()
        
        self.g = 9.81
        self.system = system
    
    def gravity(self, objects):
        
        for object in objects:
            
            if (object.check_ground() == "empty"):
                
                distance = object.check_distance((1/2 * self.g * pow(object.seconds, 2)))
                
                if (distance == "enough distance"):
                    
                    object.momentum_y += (1/2 * self.g * pow(object.seconds, 2))             

                else:
                    
                    object.momentum_y = 0
                    object.rect.y = int(self.system.height - (object.rect.y + self.system.scales.border))

if(__name__ == "__main__"):
   
    sys.exit()