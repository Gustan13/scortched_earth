import pygame

from map_maker import map_maker
from random import randrange, choice
from maps import maps
from settings import WIDTH, HEIGHT, HALF_TILE, TILE_SIZE


class LevelManager:
    def __init__(self, obstacle_group, player_group, banana_group):
        self.is_gameover = False
        self.map_maker = map_maker(obstacle_group, player_group, banana_group)
        self.og = obstacle_group
        self.pg = player_group
        self.bg = banana_group

        self.display = pygame.display.get_surface()
        self.comic_sans = pygame.font.SysFont("Comic Sans MS", int((TILE_SIZE * 2) / 3))

        self.winner = "Man"

    def restart_level(self):
        self.erase_level()
        self.map_maker.build_map(choice(maps))

    def erase_level(self):
        self.og.empty()
        self.pg.empty()
        self.bg.empty()

    def restart_screen(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_RETURN]:
            self.is_gameover = False
            self.restart_level()

        text = self.comic_sans.render(
            self.winner.upper() + " WINS!!", False, (255, 0, 0)
        )
        self.display.blit(text, (WIDTH / 2 - HALF_TILE, HEIGHT / 2 - HALF_TILE))
