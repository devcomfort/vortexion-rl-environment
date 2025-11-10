import pyxel as px

import config
from core import Game
from systems import Input
from ui import MonospaceBitmapFont
from utils import clip

APP_WIDTH = config.APP_WIDTH
APP_HEIGHT = config.APP_HEIGHT
APP_NAME = config.APP_NAME
APP_DISPLAY_SCALE = config.APP_DISPLAY_SCALE
APP_CAPTURE_SCALE = config.APP_CAPTURE_SCALE
APP_FPS = config.APP_FPS
APP_SPEED_MULTIPLIER = config.APP_SPEED_MULTIPLIER
APP_MIN_SPEED_MULTIPLIER = config.APP_MIN_SPEED_MULTIPLIER
APP_MAX_SPEED_MULTIPLIER = config.APP_MAX_SPEED_MULTIPLIER
APP_SPEED_STEP = config.APP_SPEED_STEP
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

        # 배속 제어를 위한 변수들
        self.speed_multiplier = clip(
            APP_SPEED_MULTIPLIER, APP_MIN_SPEED_MULTIPLIER, APP_MAX_SPEED_MULTIPLIER
        )
        self._update_frame_counter = 0

        px.run(self.update, self.draw)

    def update(self):
        self.input.update()

        # 배속 조정: - 키로 감소, + 키로 증가
        if px.btnp(px.KEY_MINUS) or px.btnp(px.KEY_KP_MINUS):
            self.speed_multiplier = clip(
                self.speed_multiplier - APP_SPEED_STEP,
                APP_MIN_SPEED_MULTIPLIER,
                APP_MAX_SPEED_MULTIPLIER,
            )
        elif px.btnp(px.KEY_PLUS) or px.btnp(px.KEY_EQUALS) or px.btnp(px.KEY_KP_PLUS):
            self.speed_multiplier = clip(
                self.speed_multiplier + APP_SPEED_STEP,
                APP_MIN_SPEED_MULTIPLIER,
                APP_MAX_SPEED_MULTIPLIER,
            )

        # 배속 설정에 따라 게임 로직을 여러 번 업데이트
        # 렌더링은 정상 속도로 유지되므로 시뮬레이션만 빠르게 실행됨
        speed_multiplier = self.speed_multiplier

        if speed_multiplier >= 1.0:
            # 배속: 정수 부분만큼 여러 번 업데이트
            update_count = int(speed_multiplier)
            for _ in range(max(1, update_count)):
                self.game.update()
        else:
            # 감속: 일정 간격으로 업데이트
            # 예: 0.5배속 = 2프레임마다 1번, 0.25배속 = 4프레임마다 1번
            update_interval = int(1.0 / speed_multiplier)
            self._update_frame_counter += 1
            if self._update_frame_counter >= update_interval:
                self._update_frame_counter = 0
                self.game.update()

    def draw(self):
        px.cls(0)
        self.game.draw()


if __name__ == "__main__":
    App()
