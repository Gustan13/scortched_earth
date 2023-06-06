import pygame

from player import player


class Marcelo(player):
    def __init__(self, x, y, obst_g, banana_group):
        super().__init__("marcelo", x, y, obst_g, banana_group)

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_n]:
            self.cannon_anim.play(self)
            if keys[pygame.K_m]:
                self.throw_banana()
            if keys[pygame.K_s]:
                self.change_power(-1)

        if keys[pygame.K_a]:
            if keys[pygame.K_n]:
                self.change_angle(-1)
                return

            self.walk(-1)
            self.idle_anim.mirrored = False
            self.walk_anim.mirrored = False
        elif keys[pygame.K_d]:
            if keys[pygame.K_n]:
                self.change_angle(1)
                return

            self.walk(1)
            self.idle_anim.mirrored = True
            self.walk_anim.mirrored = True

        if keys[pygame.K_w]:
            if keys[pygame.K_n]:
                self.change_power(1)
                return

            self.jump()
