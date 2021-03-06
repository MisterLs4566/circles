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

        self.momentum_x = 0
        self.momentum_y = 0

        self.grounded = False

        self.image = pygame.image.load("./sprites/ball.png")
        self.image = pygame.transform.scale(self.image, (scale_x, scale_y))
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.rect.x = pos_x
        self.rect.y = pos_y

    def update(self):
        
        self.timer += float(1000/self.system.fps)
        self.seconds = float(self.timer/1000)

        self.rect.y += self.momentum_y * self.system.dt
        self.rect.x += self.momentum_x * self.system.dt

        self.clear()

    def clear(self):

        if(self.rect.y > self.system.height):

            self.destroy()

    def destroy(self):

        self.system.sprites.remove(self)
        del self

    def check_ground(self):

        for object in self.system.sprites:
            
            if(object != self):
                
                if(self.rect.colliderect(object.rect)):
                
                    if(object.rect.y <= (self.rect.y + self.scale_y)):
                            
                            if((object.grounded == True) and (self.grounded == False)):
                                
                                self.timer = 0
                                self.momentum_y *= -0.3
                                self.momentum_y += 1
                                self.grounded = True
                                
                                return "object"
                pass

        if((self.system.height - (self.rect.y + self.system.scales.border)) < (self.scale_y + self.system.scales.border)):
            
            if(self.grounded == False):
                self.timer = 0
                self.momentum_y = 0
                self.grounded = True

                return "ground"
        
        self.grounded = False

        return "empty"

    def check_distance(self, step):
        
        if(int(self.scale_y + step >= (self.rect.y + self.system.scales.border))):

            #return int(self.system.height - (self.rect.y + self.system.scales.border))
            return "ground"

        else:

            return "enough distance"

if(__name__ == "__main__"):
    
    sys.exit()