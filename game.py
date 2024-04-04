import arcade
from arcade.tilemap import read_tmx

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


if __name__ == "__main__":
    window = GameWindow()
    arcade.run()
