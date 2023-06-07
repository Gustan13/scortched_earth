import pygame
from settings import TILE_SIZE


class tile(pygame.sprite.Sprite):
    def __init__(self, x, y, name):
        super().__init__()
        self.spawner = ""
        self.image = pygame.image.load("sprites/frames_" + name + "/" + name + "_0.gif")
        self.image = pygame.transform.scale(self.image, (TILE_SIZE, TILE_SIZE))
        self.rect = self.image.get_rect()

        self.rect.topleft = (x * TILE_SIZE, y * TILE_SIZE)


class brick(tile):
    def __init__(self, x, y, spawner, players):
        super().__init__(x, y, "bricks")
        self.spawner = spawner
        self.player_left = False
        self.players = players

    def update(self):
        if self.player_left:
            return

        if pygame.sprite.spritecollide(self, self.players, False):
            return

        self.player_left = True
