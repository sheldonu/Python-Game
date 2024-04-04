import arcade
from arcade.tilemap import read_tmx
from arcade.physics_engines import PhysicsEngineSimple

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Platformer Demo"

class GameWindow(arcade.Window):
    def __init__(self):
        super().__init__(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)

    def on_draw(self):
        arcade.start_render()
    

class GameWindow(arcade.Window):
    # ...

    def setup(self):
        self.level = read_tmx("level.tmx")



class GameWindow(arcade.Window):
    # ...

    def setup(self):
        # ...

self.physics_engine = PhysicsEngineSimple(self.player_sprite, self.level["Platforms"])


class Player(arcade.Sprite):
    def __init__(self, image, scale):
        super().__init__(image, scale)

    def update(self):
        # Update player movement and animations here
        pass




if __name__ == "__main__":
    window = GameWindow()
    arcade.run()
