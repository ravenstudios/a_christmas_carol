from constants import *


class MovementHandler():
    def __init__(self, player):
        self.player = player


    def right(self):
        if self.player.rect.center[0] < GAME_WIDTH // 2 or self.player.camera_x == GAME_WIDTH * 3:
            self.player.rect.x += self.player.speed
        if self.player.rect.center[0] > GAME_WIDTH // 2 and self.player.camera_x < GAME_WIDTH * 3:
            self.player.camera_x += self.player.speed

    def left(self):
        if self.player.rect.x > 0 and self.player.camera_x == 0 or self.player.camera_x > GAME_WIDTH * 2.9:
            self.player.rect.x -= self.player.speed
        if self.player.camera_x > 0 and self.player.rect.x < GAME_WIDTH // 2:
            self.player.camera_x -= self.player.speed

    def down(self):
        if self.player.rect.center[1] < GAME_HEIGHT // 2 or self.player.camera_y == GAME_HEIGHT:
            self.player.rect.y += self.player.speed
        if self.player.rect.center[1] > GAME_HEIGHT // 2 and self.player.camera_y < GAME_HEIGHT:
            self.player.camera_y += self.player.speed

    def up(self):
        if self.player.rect.center[1] > GAME_HEIGHT // 2 or self.player.camera_y == 0:
            self.player.rect.y -= self.player.speed
        if self.player.camera_y > 0:
            self.player.camera_y -= self.player.speed




    def update(self, player):
        player.rect.x = max(0, min(player.rect.x, GAME_WIDTH - player.rect.width))
        player.rect.y = max(0, min(player.rect.y, GAME_HEIGHT - player.rect.height))
