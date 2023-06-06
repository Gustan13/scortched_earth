import pygame
from settings import TILE_SIZE, HEIGHT, WIDTH, HALF_TILE


class PauseMenu:
    def __init__(self) -> None:
        self.is_paused = False
        self.display = pygame.display.get_surface()
        self.comic_sans = pygame.font.SysFont("Comic Sans MS", int((TILE_SIZE * 2) / 3))
        self.text = self.comic_sans.render("PAUSED", False, (255, 0, 0))

        self.is_pressed = False

    def pause(self):
        keys = pygame.key.get_pressed()

        if keys[pygame.K_ESCAPE]:
            if self.is_pressed == False:
                self.is_pressed = True
                if self.is_paused:
                    self.is_paused = False
                else:
                    self.is_paused = True
        else:
            self.is_pressed = False

    def update(self):
        self.pause()

        if self.is_paused:
            self.display.blit(
                self.text, (WIDTH / 2 - HALF_TILE, HEIGHT / 2 - HALF_TILE)
            )
