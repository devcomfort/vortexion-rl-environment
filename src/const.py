"""
Game configuration constants.

This module contains all game configuration values including:
- Application settings (window size, FPS, etc.)
- Game mechanics (lives, weapons, scores, damage)
- Stage and music configuration
- Entity types and color palette
"""

from enum import Enum, IntEnum, auto

# ============================================================================
# Application Configuration
# ============================================================================

APP_VERSION = "1.0"  # Used in: game_state_titles.py (displayed on title screen)

APP_WIDTH = 256  # Used in: main.py (window width), player.py (boundary check), enemy_shot.py, player_shot.py (boundary check)

APP_HEIGHT = 192  # Used in: main.py (window height), player.py (boundary check)

APP_NAME = "VORTEXION"  # Used in: main.py (window title)

APP_FPS = 60  # Used in: main.py (frames per second)

APP_DISPLAY_SCALE = 2  # Used in: main.py (display scaling factor)

APP_CAPTURE_SCALE = 2  # Used in: main.py (capture scaling factor)

APP_GFX_FILE = "gfx.png"  # Used in: main.py (graphics resource file)

SOUNDS_RES_FILE = "sounds.pyxres"  # Used in: main.py (sounds resource file)

# ============================================================================
# Stage Configuration
# ============================================================================


class StageNum(IntEnum):
    """Stage number enumeration. Used in: game_vars.py, game_state_stage.py"""

    STAGE_1 = auto()  # = 1
    STAGE_2 = auto()  # vortex
    STAGE_3 = auto()
    STAGE_4 = auto()  # vortex
    STAGE_5 = auto()


FINAL_STAGE = StageNum.STAGE_5  # Used in: game_vars.py (stage progression check), game_state_stage.py (final stage check)

STAGE_MUSIC_FILES = {
    # Used in: game_state_stage.py (stage music loading)
    StageNum.STAGE_1: "music_stage_1.json",
    StageNum.STAGE_2: "music_vortex.json",
    StageNum.STAGE_3: "music_stage_3.json",
    StageNum.STAGE_4: "music_vortex.json",
    StageNum.STAGE_5: "music_stage_5.json",
}

MUSIC_GAME_COMPLETE = "music_game_complete.json"  # Used in: game_state_complete.py

MUSIC_GAME_OVER = "music_game_over.json"  # Used in: game_state_stage.py

MUSIC_BOSS = "music_boss.json"  # Used in: game_state_stage.py

MUSIC_STAGE_CLEAR = "music_stage_clear.json"  # Used in: game_state_stage.py

# ============================================================================
# Entity Types
# ============================================================================


class EntityType(Enum):
    """
    Entity type enumeration.
    Used in: player.py, enemy.py, enemy_shot.py, player_shot.py, powerup.py, stage_background.py
    (collision detection and entity identification)
    """

    PLAYER = 0
    PLAYER_SHOT = auto()
    ENEMY = auto()
    ENEMY_SHOT = auto()
    POWERUP = auto()
    BACKGROUND = auto()


# ============================================================================
# Game Mechanics Configuration
# ============================================================================

STARTING_LIVES = 3  # Used in: game_vars.py (initial lives count)

MAX_LIVES = 9  # Used in: game_vars.py (maximum lives cap)

MAX_WEAPONS = 3  # Used in: game_vars.py (weapon array size), hud.py (weapon display loop), powerup.py (weapon type cycling)

MAX_WEAPON_LEVEL = (
    5  # Used in: game_vars.py (weapon level cap), hud.py (weapon level display)
)

WEAPON_NAMES = ["A", "B", "C"]  # Used in: hud.py (weapon name display)

MAX_SCORE = 999999  # Used in: game_vars.py (score cap)

ENEMY_SCORE_NORMAL = 100  # Used in: enemy.py (normal enemy score value)

ENEMY_SCORE_BOSS = (
    5000  # Used in: enemy_k.py, enemy_l.py, enemy_m.py (boss enemy score value)
)

PLAYER_SHOT_DAMAGE = 1  # Used in: enemy.py (damage calculation)

BOMB_DAMAGE = 30  # Used in: enemy.py (bomb damage calculation)

# ============================================================================
# Graphics Configuration
# ============================================================================

MAX_COLOURS = 16  # Used in: powerup.py (color cycling)

PALETTE = [
    # Used in: main.py (color palette initialization)
    0xFF00FF,  # transparent
    0x000000,
    0x21C842,
    0x5EDC78,
    0x5455ED,
    0x7D76FC,
    0xD4524D,
    0x42EBF5,
    0xFC5554,
    0xFF7978,
    0xD4C154,
    0xE6CE80,
    0x21B03B,
    0xC95BBA,
    0xCCCCCC,
    0xFFFFFF,
]
