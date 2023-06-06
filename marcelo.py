import pygame

from player import player


class Marcelo(player):
    def __init__(self, x, y, obst_g, banana_group, player_group):
        super().__init__("marcelo", x, y, obst_g, banana_group, player_group)
        self.is_pressed = False

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RSHIFT]:
            self.cannon_anim.play(self)
            if keys[pygame.K_RCTRL]:
                if self.is_pressed == False:
                    self.throw_banana()
                    self.is_pressed = True
            else:
                self.is_pressed = False
            if keys[pygame.K_w]:
                self.change_power(1)
            elif keys[pygame.K_s]:
                self.change_power(-1)
            elif keys[pygame.K_d]:
                self.change_angle(1)
            elif keys[pygame.K_a]:
                self.change_angle(-1)

        else:
            if keys[pygame.K_w]:
                self.jump()

            if keys[pygame.K_d]:
                self.walk(1)
                self.idle_anim.mirrored = True
                self.walk_anim.mirrored = True
            elif keys[pygame.K_a]:
                self.walk(-1)
                self.idle_anim.mirrored = False
                self.walk_anim.mirrored = False
