import pygame
from animation import Animation

from settings import TILE_SIZE, ACCELERATION, FPS


class player(pygame.sprite.Sprite):
    def __init__(self, name, x, y, obst_g):
        super().__init__()

        self.idle_anim = Animation(name, 1, 1, TILE_SIZE)
        self.walk_anim = Animation(name, 4, 10, TILE_SIZE)

        self.image = pygame.image.load("sprites/frames_banana/placeholder.gif")
        self.rect = self.image.get_rect()

        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)

        self.obst_g = obst_g

        self.y_speed = 0

    def input(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_LEFT]:
            self.walk(-1)
        if keys[pygame.K_RIGHT]:
            self.walk(1)

    def walk(self, dir):
        self.rect.centerx += dir * 1

        collisions = pygame.sprite.spritecollide(self, self.obst_g, False)
        for collision in collisions:
            if dir == 1:
                self.rect.right = collision.rect.left
            else:
                self.rect.left = collision.rect.right

    def fall(self):
        self.y_speed += 9.8 / FPS
        self.rect.y += self.y_speed

        collisions = pygame.sprite.spritecollide(self, self.obst_g, False)

        for collision in collisions:
            self.rect.bottom = collision.rect.top
            self.y_speed = 0

    def update(self):
        self.walk_anim.play(self)
        self.input()
        self.fall()
