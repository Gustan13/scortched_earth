import pygame
from settings import WIDTH


class Hud:
    def __init__(self, player_group) -> None:
        self.player_group = player_group

    def update(self):
        for i, player in enumerate(self.player_group.sprites()):
            pygame.draw.line(
                pygame.display.get_surface(),
                (0, 0, 0),
                (50 + (WIDTH - 120) * i, 100),
                (50 + (WIDTH - 120) * i + player.cos * 30, 100 + player.sin * 30),
                2,
            )
