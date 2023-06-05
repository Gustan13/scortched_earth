from tile import tile
from settings import TILE_SIZE, HALF_TILE, WIDTH, HEIGHT


class map_maker:
    def __init__(self, obstacle_group, player_group) -> None:
        self.obstacle_group = obstacle_group
        self.player_group = player_group

    def build_map(self, map_array):
        for i, row in enumerate(map_array):
            for j, num in enumerate(row):
                if num == 1:
                    self.obstacle_group.add(tile(j, i, "building"))
                elif num == 2:
                    self.obstacle_group.add(tile(j, i, "floor"))
                elif num == 3:
                    self.obstacle_group.add(tile(j, i, "marcelo"))
                elif num == 4:
                    self.obstacle_group.add(tile(j, i, "binder"))
