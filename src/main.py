import pyxel as px

import const
from core import Game
from systems import Input
from ui import MonospaceBitmapFont

APP_WIDTH = const.APP_WIDTH
APP_HEIGHT = const.APP_HEIGHT
APP_NAME = const.APP_NAME
APP_DISPLAY_SCALE = const.APP_DISPLAY_SCALE
APP_CAPTURE_SCALE = const.APP_CAPTURE_SCALE
APP_FPS = const.APP_FPS
APP_GFX_FILE = const.APP_GFX_FILE
PALETTE = const.PALETTE
SOUNDS_RES_FILE = const.SOUNDS_RES_FILE


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
