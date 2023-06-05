import pygame
from settings import FPS, WIDTH, HEIGHT
from map_maker import map_maker
from maps import map_1


class Game:
    def __init__(self) -> None:
        pygame.init()

        self.isRunning = True
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.obstacle_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()

        self.game_loop()

    def draw(self):
        self.display.fill((0, 180, 255))

        self.obstacle_group.draw(self.display)

    def flip(self):
        pygame.display.flip()
        self.clock.tick(FPS)

    def game_loop(self):
        map_m = map_maker(self.obstacle_group, self.player_group)

        map_m.build_map(map_1)

        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.draw()
            self.flip()

        pygame.quit()


Game()
