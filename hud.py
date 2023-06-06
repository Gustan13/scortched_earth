import pygame
from settings import WIDTH

pygame.font.init()
comic_sans = pygame.font.SysFont("Comic Sans MS", 30)


class Hud:
    def __init__(self, player_group) -> None:
        self.player_group = player_group
        self.display = pygame.display.get_surface()

    def update(self):
        for i, player in enumerate(self.player_group.sprites()):
            pygame.draw.line(
                self.display,
                (0, 0, 0),
                (50 + (WIDTH - 120) * i, 100),
                (50 + (WIDTH - 120) * i + player.cos * 30, 100 + player.sin * 30),
                2,
            )
            text_surface = comic_sans.render(str(player.power), False, (0, 0, 0))
            self.display.blit(text_surface, (100 + (WIDTH - 120) * i - i * 125, 100))
