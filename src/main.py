import pyxel as px

import config
from core import Game
from systems import Input
from ui import MonospaceBitmapFont

APP_WIDTH = config.APP_WIDTH
APP_HEIGHT = config.APP_HEIGHT
APP_NAME = config.APP_NAME
APP_DISPLAY_SCALE = config.APP_DISPLAY_SCALE
APP_CAPTURE_SCALE = config.APP_CAPTURE_SCALE
APP_FPS = config.APP_FPS
APP_GFX_FILE = config.APP_GFX_FILE
PALETTE = config.PALETTE
SOUNDS_RES_FILE = config.SOUNDS_RES_FILE


class App:
    def __init__(self) -> None:
        px.init(
            APP_WIDTH,
            APP_HEIGHT,
            title=APP_NAME,
            fps=APP_FPS,
            display_scale=APP_DISPLAY_SCALE,
            capture_scale=APP_CAPTURE_SCALE,
        )

        px.colors.from_list(PALETTE)
        px.images[0].load(0, 0, "assets/" + APP_GFX_FILE)
        px.load(
            "assets/" + SOUNDS_RES_FILE,
            excl_images=True,
            excl_tilemaps=True,
            excl_musics=True,
        )

        self.main_font = MonospaceBitmapFont()
        self.input = Input()

        self.game = Game(self)

        px.run(self.update, self.draw)

    def update(self):
        self.input.update()
        self.game.update()

    def draw(self):
        px.cls(0)
        self.game.draw()


if __name__ == "__main__":
    App()
