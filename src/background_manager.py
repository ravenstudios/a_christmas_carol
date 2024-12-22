import pygame
from constants import *
import os


class BackgroundManager():
    def __init__(self):
        path = os.path.join(os.path.dirname(__file__), "..", "assets/imgs/London1.png")

        self.bk = Background(path, 3)


    def update(self, cam_offset):
        self.bk.update(cam_offset)


    def draw(self, surface):
        self.bk.draw(surface)



class Background():
    def __init__(self, file, scroll_speed):
        self.scroll_speed = scroll_speed
        self.image = pygame.image.load(file).convert_alpha()
        scaled_width, scaled_height = self.image.get_size()
        self.image1 = pygame.transform.scale(self.image, (scaled_width * SCALER, scaled_height * SCALER))
        self.image2 = pygame.transform.scale(self.image, (scaled_width * SCALER, scaled_height * SCALER))
        self.rect1 = self.image.get_rect()
        self.rect1.topleft = (0, 0)
        self.rect2 = self.image.get_rect()
        self.rect2.topleft = (self.rect1.width * SCALER, 0)




    def draw(self, surface):
        surface.blit(self.image1, (self.rect1.x, self.rect1.y))
        surface.blit(self.image2, (self.rect2.x, self.rect2.y))




    def update(self, cam_offset):
        self.rect1.x = (cam_offset[0])
        self.rect1.y = (cam_offset[1])
        
        # self.rect1.x = min(self.rect1.x, 0)
        # self.rect1.y = min(self.rect1.y, 0)

        self.rect2.x = (cam_offset[0] + self.rect1.width * SCALER)
        self.rect2.y = (cam_offset[1])
        # print(f"rect2.x:{self.rect2.x}")
        # self.rect1.x = min(self.rect1.x, 0)
        # self.rect1.y = min(self.rect1.y, 0)

        # self.y = min(0, max(GAME_HEIGHT * SCALER, self.y))
