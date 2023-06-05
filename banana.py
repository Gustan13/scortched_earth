from math import sin, cos
import pygame
from animation import Animation
from settings import TILE_SIZE, FPS, HEIGHT


class Banana(pygame.sprite.Sprite):
    def __init__(self, banana_group, obstacle_group, angle, power, position) -> None:
        super().__init__(banana_group)

        self.banana_spin = Animation("banana", 4, 10, TILE_SIZE)

        self.image = pygame.image.load("sprites/frames_banana/banana_0.gif")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))

        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self.banana_group = banana_group
        self.obstacle_group = obstacle_group

        self.y_speed = 0

        self.initial_xs = cos(angle) * power
        self.initial_ys = -sin(angle) * power

        self.angles = pygame.math.Vector2(cos(angle) * power, -sin(angle) * power)
        self.angles.normalize()

        print(self.initial_xs, self.initial_ys)

    def collision(self):
        if pygame.sprite.spritecollide(self, self.obstacle_group, True):
            self.kill()

        if self.rect.y > HEIGHT:
            self.kill()

    def move(self):
        self.angles.y += 9.8 / FPS

        self.rect.topleft += self.angles

        self.collision()

    def update(self):
        self.move()
        self.banana_spin.play(self)
