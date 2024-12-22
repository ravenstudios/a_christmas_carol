import pygame
import os
from constants import *
class Wall(object):
    """docstring for Wall."""

    def __init__(self):
        self.image_path = os.path.join(os.path.dirname(__file__), "..", "..", "assets/imgs/London.png")
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (640 * 4, 320 * 4))
        # self.image.set_alpha(16)



    def draw(self, surface):
        surface.blit(self.image, (0, 0))
