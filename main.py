import sys
import pygame;
from pygame.locals import *
from lib.sphere import Sphere
from lib.scales import Scales
from lib.physics import Physics

pygame.init()

class System():
    
    def __init__(self):
        
        super().__init__()
        
        self.fps = 60
        self.framerate = 0
        self.sprites = pygame.sprite.Group()


        self.width = 600
        self.height = 600

        self.window = pygame.display.set_mode((self.width, self.height))
        self.clock = pygame.time.Clock()

        self.run = False

        self.scales = Scales()
        self.physics = Physics()

    def main(self):
        
        self.run = True
    
    def update(self):

        self.framerate = int(self.clock.get_fps())
        pygame.display.set_caption(str(self.framerate))

        if(self.framerate < self.fps-30):
            self.clear_sprites()
    
    def clear_sprites(self):
    
        for object in self.sprites:
                del object

        self.sprites.empty()

            

if (__name__ == "__main__"):

    system = System()
    system.main()



while(system.run == True):

    pygame.display.update()

    system.clock.tick(system.fps)
    system.update()

    system.window.fill((255, 255, 255))

    system.sprites.draw(system.window)
    system.sprites.update()

    system.physics.gravity(system.sprites)

    for event in pygame.event.get():
        
        if(event.type == pygame.MOUSEBUTTONDOWN):

            mouse_x = pygame.mouse.get_pos()[0]
            mouse_y = pygame.mouse.get_pos()[1]

            scale = system.scales.scale_sphere
            
            sphere = Sphere(system, mouse_x - scale/2, mouse_y - scale/2, scale, scale)
            
            system.sprites.add(sphere)

        elif(event.type == pygame.KEYDOWN):
            
            if(event.key == pygame.K_c):

                system.clear_sprites()

        elif(event.type == pygame.QUIT):
            
            sys.exit()

