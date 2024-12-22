from constants import *

class Camera(object):


    def __init__(self):
        pass

    def update_offset(self, player):
        scl = 2
        x = -player.camera_x
        y = -player.camera_y
        return (x, y)
