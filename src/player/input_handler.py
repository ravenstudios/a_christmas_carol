import pygame


class InputHandler():

    def __init__(self, player):
        self.player = player


    def check_keyboard(self, events):
        for event in events:
            if event.type == pygame.JOYBUTTONDOWN:
                    button = event.button
                    if button == 13:
                        self.player.movement_handler.left()

                    if button == 14:
                        self.player.movement_handler.right()



            # if event.type == pygame.KEYDOWN:
            #     keys = pygame.key.get_pressed()
            #
            #     if keys[pygame.K_UP]:
            #         self.player.movement_handler.up()
            #
            #     if keys[pygame.K_DOWN]:
            #         self.player.movement_handler.down()




        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.player.movement_handler.left()

        if keys[pygame.K_RIGHT]:
            self.player.movement_handler.right()

        if keys[pygame.K_UP]:
            self.player.movement_handler.up()

        if keys[pygame.K_DOWN]:
            self.player.movement_handler.down()
