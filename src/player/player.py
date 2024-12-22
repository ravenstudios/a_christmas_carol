import pygame
from constants import *
import main_entity

import os
from player import (sound_manager, input_handler, movement_handler, collision_handler, animation_handler)

class Player(main_entity.Main_entity):
    def __init__(self, x, y):
        super().__init__(x, y)

        self.speed = 10
        self.camera_x = 0
        self.camera_y = 0

        self.y_sprite_sheet_index = 0

        # self.sound_manager = sound_manager.SoundManager()
        self.input_handler = input_handler.InputHandler(self)
        self.movement_handler = movement_handler.MovementHandler(self)
        self.collision_handler = collision_handler.CollisionHandler(self)
        self.animation_handler = animation_handler.AnimationHandler(self)



    def update(self, events, cam_offset):
        self.input_handler.check_keyboard(events)
        # self.update_cam_offset(cam_offset)
        # self.cam_offset = cam_offset
        # print(self.rect.x)
        self.movement_handler.update(self)
