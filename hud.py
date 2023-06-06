import pygame
from settings import WIDTH, TILE_SIZE


class Hud:
    def __init__(self, player_group) -> None:
        self.player_group = player_group
        self.display = pygame.display.get_surface()
        self.comic_sans = pygame.font.SysFont("Comic Sans MS", int((TILE_SIZE * 2) / 3))

    def update(self):
        for i, player in enumerate(self.player_group.sprites()):
            pygame.draw.line(
                self.display,
                (0, 0, 0),
                (TILE_SIZE + (WIDTH - 120) * i, TILE_SIZE * 2),
                (
                    TILE_SIZE + (WIDTH - 120) * i + player.cos * 30,
                    TILE_SIZE * 2 + player.sin * 30,
                ),
                2,
            )
            text_surface = self.comic_sans.render(str(player.power), False, (0, 0, 0))
            self.display.blit(text_surface, (100 + (WIDTH - 120) * i - i * 125, 100))
