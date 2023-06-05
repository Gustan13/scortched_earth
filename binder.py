import pygame

from player import player


class Binder(player):
    def __init__(self, x, y, obst_g, banana_group):
        super().__init__("binder", x, y, obst_g, banana_group)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_2]:
            self.cannon_anim.play(self)
            if keys[pygame.K_3]:
                self.throw_banana()

        if keys[pygame.K_LEFT]:
            if keys[pygame.K_2]:
                self.change_angle(-1)
                return

            self.walk(-1)
            self.idle_anim.mirrored = False
            self.walk_anim.mirrored = False
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_2]:
                self.change_angle(1)
                return

            self.walk(1)
            self.idle_anim.mirrored = True
            self.walk_anim.mirrored = True
