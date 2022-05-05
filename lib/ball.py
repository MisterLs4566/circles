import sys
import pygame
from pygame.locals import *

pygame.init()

class Ball(pygame.sprite.Sprite):

    def  __init__(self, pos_x, pos_y, scale_x, scale_y):

        super().__init__()

        self.pos_x = pos_x
        self.pos_y = pos_y
        self.scale_x = scale_x
        self.scale_y = scale_y

        self.image = pygame.Surface((scale_x, scale_y))
        pygame.transform.scale(self.image, (scale_x, scale_y))
        self.image.fill((255, 255, 255))
        pygame.draw.circle(self.image, (0, 0, 0), (scale_x, scale_y), 25)
        self.rect = self.image.get_rect()
        self.rect.center = (0, 0)
        self.rect.x = pos_x
        self.rect.y = pos_y


if(__name__ == "__main__"):
    sys.exit()