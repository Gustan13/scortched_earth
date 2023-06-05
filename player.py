import pygame
from animation import Animation
from banana import Banana

from math import pi

from settings import TILE_SIZE, ACCELERATION, FPS


class player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, obst_g, banana_group):
        super().__init__()

        self.idle_anim = Animation(name, 1, 1, TILE_SIZE)
        self.walk_anim = Animation(name, 4, 10, TILE_SIZE)
        self.cannon_anim = Animation("banana", 4, 10, TILE_SIZE)

        self.image = pygame.image.load("sprites/frames_banana/placeholder.gif")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()

        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)

        self.obst_g = obst_g
        self.banana_group = banana_group

        self.y_speed = 0

        self.mirrored = True

        self.angle = pi / 2
        self.power = 5

        self.timer = 0
        self.timer_set = 20

    def input(self):
        pass

    def walk(self, dir):
        self.rect.centerx += dir * TILE_SIZE / 32

        collisions = pygame.sprite.spritecollide(self, self.obst_g, False)
        for collision in collisions:
            if dir == 1:
                self.rect.right = collision.rect.left
            else:
                self.rect.left = collision.rect.right
            return

        self.walk_anim.play(self)

    def fall(self):
        self.y_speed += 9.8 / FPS
        self.rect.y += self.y_speed

        collisions = pygame.sprite.spritecollide(self, self.obst_g, False)

        for collision in collisions:
            self.rect.bottom = collision.rect.top
            self.y_speed = 0

    def change_angle(self, dir):
        if self.angle > pi * 2:
            self.angle = 0

        if self.angle < 0:
            self.angle = pi * 2

        self.angle -= dir * 0.01
        # print(self.angle)

    def throw_banana(self):
        if self.timer <= 0:
            Banana(
                self.banana_group,
                self.obst_g,
                self.angle,
                self.power,
                self.rect.topleft,
            )
            self.timer = self.timer_set
        else:
            self.timer -= 1

    def update(self):
        self.idle_anim.play(self)
        self.input()
        self.fall()
