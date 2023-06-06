from math import sin, cos
import pygame
from animation import Animation
from settings import TILE_SIZE, HALF_TILE, FPS, HEIGHT


class Banana(pygame.sprite.Sprite):
    def __init__(
        self,
        banana_group,
        obstacle_group,
        player_group,
        thrower,
        angle,
        power,
        position,
    ) -> None:
        super().__init__(banana_group)

        self.thrower = thrower

        self.banana_spin = Animation("banana", 4, 10, HALF_TILE)

        self.image = pygame.image.load("sprites/frames_banana/banana_0.gif")
        self.image = pygame.transform.scale(self.image, (HALF_TILE, HALF_TILE))

        self.rect = self.image.get_rect()
        self.rect.topleft = position

        self.banana_group = banana_group
        self.obstacle_group = obstacle_group
        self.player_group = player_group

        self.y_speed = 0

        self.initial_xs = cos(angle) * power
        self.initial_ys = -sin(angle) * power

        self.angles = pygame.math.Vector2(cos(angle) * power, -sin(angle) * power)
        self.angles.normalize()

    def collision(self):
        if pygame.sprite.spritecollide(self, self.obstacle_group, True):
            self.kill()

        players_collided = pygame.sprite.spritecollide(self, self.player_group, False)
        for player in players_collided:
            if player.name != self.thrower:
                self.kill()
                player.kill()

        if self.rect.y > HEIGHT:
            self.kill()

    def move(self):
        self.angles.y += 9.8 / FPS

        self.rect.topleft += self.angles

        self.collision()

    def update(self):
        self.move()
        self.banana_spin.play(self)
