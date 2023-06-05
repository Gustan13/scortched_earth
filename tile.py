import pygame
from settings import TILE_SIZE


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.image = pygame.image.load("sprites/frames_banana/banana_0.gif")
        self.rect = self.image.get_rect()

        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)
