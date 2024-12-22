import pygame
import os

class Marley(object):
    """docstring for Marley."""

    def __init__(self):
        self.image_path = os.path.join(os.path.dirname(__file__), "..", "assets/imgs/Char-Sheet.png")
        self.image = pygame.image.load(self.image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, (128, 128))
        self.image.set_alpha(128)
    def draw(self, surface):
        surface.blit(self.image, (0, 0))
