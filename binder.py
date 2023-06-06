import pygame

from player import player
from enum import Enum


class Binder(player):
    def __init__(self, x, y, obst_g, banana_group, player_group):
        super().__init__("binder", x, y, obst_g, banana_group, player_group)
        self.is_pressed = False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_KP2]:
            self.cannon_anim.play(self)
            if keys[pygame.K_KP3]:
                if self.is_pressed == False:
                    self.throw_banana()
                    self.is_pressed = True
            else:
                self.is_pressed = False

            if keys[pygame.K_UP]:
                self.change_power(1)
            elif keys[pygame.K_DOWN]:
                self.change_power(-1)
            elif keys[pygame.K_RIGHT]:
                self.change_angle(1)
            elif keys[pygame.K_LEFT]:
                self.change_angle(-1)

        else:
            if keys[pygame.K_UP]:
                self.jump()

            if keys[pygame.K_RIGHT]:
                self.walk(1)
                self.idle_anim.mirrored = True
                self.walk_anim.mirrored = True
            elif keys[pygame.K_LEFT]:
                self.walk(-1)
                self.idle_anim.mirrored = False
                self.walk_anim.mirrored = False
