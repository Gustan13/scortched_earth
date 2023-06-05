import pygame
from settings import FPS


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.isRunning = True
        self.display = pygame.display.set_mode((500, 500))
        self.clock = pygame.time.Clock()

        self.game_loop()

        pass

    def game_loop(self):
        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.display.fill((0, 0, 0))
            pygame.display.flip()
            self.clock.tick(FPS)

        pygame.quit()


Game()
