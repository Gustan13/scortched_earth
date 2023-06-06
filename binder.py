import pygame

from player import player
from enum import Enum


class Binder(player):
    def __init__(self, x, y, obst_g, banana_group, player_group):
        super().__init__("binder", x, y, obst_g, banana_group, player_group)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_KP2]:
            self.cannon_anim.play(self)
            if keys[pygame.K_KP3]:
                self.throw_banana()
            if keys[pygame.K_DOWN]:
                self.change_power(-1)

        if keys[pygame.K_UP]:
            if keys[pygame.K_KP2]:
                self.change_power(1)
                return

            self.jump()

        if keys[pygame.K_LEFT]:
            if keys[pygame.K_KP2]:
                self.change_angle(-1)
                return

            self.walk(-1)
            self.idle_anim.mirrored = False
            self.walk_anim.mirrored = False
        elif keys[pygame.K_RIGHT]:
            if keys[pygame.K_KP2]:
                self.change_angle(1)
                return

            self.walk(1)
            self.idle_anim.mirrored = True
            self.walk_anim.mirrored = True
