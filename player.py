import pygame
from animation import Animation
from banana import Banana
from tile import brick

from math import pi, sin, cos

from settings import TILE_SIZE, HALF_TILE, WIDTH, HEIGHT, FPS


class player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, obst_g, banana_group, player_group):
        super().__init__([player_group])

        self.name = name

        self.idle_anim = Animation(name, 1, 1, TILE_SIZE)
        self.walk_anim = Animation(name, 4, 10, TILE_SIZE)
        self.cannon_anim = Animation("banana", 4, 10, TILE_SIZE)

        self.image = pygame.image.load("sprites/frames_banana/placeholder.gif")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()

        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)

        self.obst_g = obst_g
        self.banana_group = banana_group
        self.player_group = player_group

        self.y_speed = 0

        self.mirrored = True

        self.angle = pi / 2
        self.power = 50

        self.banana_amount = 5
        self.reload_timer = 60

        self.cos = 0
        self.sin = 0

        self.is_grounded = True

        self.spawn = self.rect.topleft

        self.spawned_brick = False

    def input(self):
        pass

    def walk(self, dir):
        self.rect.centerx += dir * TILE_SIZE / 32

        if dir == 1:
            self.mirrored = True
        else:
            self.mirrored = False

        collisions = pygame.sprite.spritecollide(self, self.obst_g, False)
        for collision in collisions:
            if collision.spawner == self.name:
                if not collision.player_left:
                    continue

            if dir == 1:
                self.rect.right = collision.rect.left
            else:
                self.rect.left = collision.rect.right
            return

        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.left < 0:
            self.rect.left = 0

        self.walk_anim.play(self)

    def fall(self):
        self.y_speed += 9.8 / FPS
        self.rect.y += self.y_speed

        self.is_grounded = False

        collisions = pygame.sprite.spritecollide(self, self.obst_g, False)

        for collision in collisions:
            if collision.spawner == self.name:
                if not collision.player_left:
                    continue

            if (
                self.rect.top < collision.rect.bottom
                and self.rect.bottom > collision.rect.bottom
            ):
                self.rect.top = collision.rect.bottom
                self.y_speed = 2
            elif (
                self.rect.bottom > collision.rect.top
                and self.rect.top < collision.rect.top
            ):
                self.rect.bottom = collision.rect.top
                self.y_speed = 0
                self.is_grounded = True

        if self.rect.y > HEIGHT:
            self.kill()

    def change_angle(self, dir):
        if self.angle > pi * 2:
            self.angle = 0

        if self.angle < 0:
            self.angle = pi * 2

        self.angle -= dir * 0.05
        # print(self.angle)

    def change_power(self, mag):
        self.power += mag

        if self.power > 100:
            self.power = 100
        elif self.power < 1:
            self.power = 1

    def jump(self):
        if self.is_grounded:
            self.y_speed = -6

    def throw_banana(self):
        if self.banana_amount < 1:
            return

        Banana(
            self.banana_group,
            self.obst_g,
            self.player_group,
            self.name,
            self.angle,
            self.power / 10,
            self.rect.topleft,
        )
        self.banana_amount -= 1

    def build(self):
        if self.mirrored:
            self.obst_g.add(
                brick(
                    (self.rect.x + TILE_SIZE + HALF_TILE) // TILE_SIZE,
                    self.rect.y // TILE_SIZE,
                    self.name,
                    self.player_group,
                )
            )
        else:
            self.obst_g.add(
                brick(
                    (self.rect.x + HALF_TILE - TILE_SIZE) // TILE_SIZE,
                    self.rect.y // TILE_SIZE,
                    self.name,
                    self.player_group,
                )
            )

    def update(self):
        self.idle_anim.play(self)
        self.input()
        self.fall()

        self.cos = cos(self.angle)
        self.sin = -sin(self.angle)

        if self.banana_amount < 1:
            self.reload_timer -= 1

        if self.reload_timer < 1:
            self.reload_timer = 60
            self.banana_amount = 5
