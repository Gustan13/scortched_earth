import pygame
from settings import FPS, WIDTH, HEIGHT
from level_manager import LevelManager
from hud import Hud
from pause_menu import PauseMenu


class Game:
    def __init__(self) -> None:
        pygame.init()
        pygame.font.init()

        self.isRunning = True
        self.display = pygame.display.set_mode((WIDTH, HEIGHT))
        self.clock = pygame.time.Clock()

        self.obstacle_group = pygame.sprite.Group()
        self.player_group = pygame.sprite.Group()
        self.banana_group = pygame.sprite.Group()

    def update(self):
        self.obstacle_group.update()
        self.player_group.update()
        self.banana_group.update()

    def draw(self):
        self.obstacle_group.draw(self.display)
        self.player_group.draw(self.display)
        self.banana_group.draw(self.display)

    def flip(self):
        pygame.display.update()
        self.clock.tick(FPS)
        self.display.fill((0, 180, 255))

    def game_loop(self):
        level_manager = LevelManager(
            self.obstacle_group, self.player_group, self.banana_group
        )
        hud = Hud(self.player_group)
        pause_menu = PauseMenu()

        level_manager.restart_level()

        while self.isRunning:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.isRunning = False

            self.draw()

            if level_manager.is_gameover == False:
                if len(self.player_group.sprites()) < 2:
                    level_manager.is_gameover = True
                    level_manager.winner = self.player_group.sprites()[0].name

                if pause_menu.is_paused == False:
                    self.update()

                hud.update()
                pause_menu.update()
            else:
                level_manager.restart_screen()

            self.flip()

        pygame.quit()


game = Game()
game.game_loop()
