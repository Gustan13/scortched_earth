import pygame
from pygame.sprite import _Group


class player(pygame.sprite.Sprite):
    def __init__(self, name, groups):
        super().__init__(groups)
