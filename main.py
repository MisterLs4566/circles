import sys
import pygame;
from pygame.locals import *
from lib.ball import Ball

pygame.init()

fps = 60

sprites = pygame.sprite.Group()

class System(pygame.sprite.Sprite):
    
    def __init__(self):
        
        super().__init__()
        
        self.window = pygame.display.set_mode((600, 600))
        self.clock = pygame.time.Clock()

        self.run = False
        self.g = 9,81

    def main(self):
        
        self.run = True
    
    def update(self):

        pass


if (__name__ == "__main__"):

    system = System()
    system.main()



while(system.run == True):

    pygame.display.update()

    system.clock.tick(fps)

    system.update()

    system.window.fill((255, 255, 255))

    sprites.draw(system.window)

    for event in pygame.event.get():
        
        if(event.type == pygame.MOUSEBUTTONDOWN):

            ball = Ball(10, 10, 50, 50)
            sprites.add(ball)

        if(event.type == pygame.QUIT):
            
            sys.exit()
