"""
Game configuration loader using Python configparser.

This module loads configuration from INI files using Python's standard
library configparser module, providing a simple and standard way to
manage game configuration.
"""

import configparser
from enum import Enum, IntEnum, auto
from pathlib import Path

# Configuration file path (always in src/ directory)
# The config.ini file is copied from project root during build process
CONFIG_FILE = Path(__file__).parent / "config.ini"

# Global config parser instance
_config = configparser.ConfigParser()

# Load configuration
if not CONFIG_FILE.exists():
    raise FileNotFoundError(
        f"Configuration file not found: {CONFIG_FILE}\n"
        f"Please run 'just build' or 'just package' to copy config.ini from project root."
    )
_config.read(CONFIG_FILE)

# ============================================================================
# Application Configuration
# ============================================================================

APP_VERSION = _config.get("app", "version")
APP_WIDTH = _config.getint("app", "width")
APP_HEIGHT = _config.getint("app", "height")
APP_NAME = _config.get("app", "name")
APP_FPS = _config.getint("app", "fps")
APP_SPEED_MULTIPLIER = _config.getfloat("app", "speed_multiplier", fallback=1.0)
APP_MIN_SPEED_MULTIPLIER = _config.getfloat(
    "app", "min_speed_multiplier", fallback=0.25
)
APP_MAX_SPEED_MULTIPLIER = (
    _config.getfloat("app", "max_speed_multiplier", fallback=None)
    if _config.get("app", "max_speed_multiplier", fallback="").strip()
    else None
)
APP_SPEED_STEP = _config.getfloat("app", "speed_step", fallback=0.25)
APP_DISPLAY_SCALE = _config.getint("app", "display_scale")
APP_CAPTURE_SCALE = _config.getint("app", "capture_scale")
APP_GFX_FILE = _config.get("app", "gfx_file")
SOUNDS_RES_FILE = _config.get("app", "sounds_res_file")

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


FINAL_STAGE = StageNum(_config.getint("stage", "final_stage"))

# Stage music files mapping
STAGE_MUSIC_FILES = {
    StageNum.STAGE_1: _config.get("stage", "stage_music_1"),
    StageNum.STAGE_2: _config.get("stage", "stage_music_2"),
    StageNum.STAGE_3: _config.get("stage", "stage_music_3"),
    StageNum.STAGE_4: _config.get("stage", "stage_music_4"),
    StageNum.STAGE_5: _config.get("stage", "stage_music_5"),
}

MUSIC_GAME_COMPLETE = _config.get("stage", "music_game_complete")
MUSIC_GAME_OVER = _config.get("stage", "music_game_over")
MUSIC_BOSS = _config.get("stage", "music_boss")
MUSIC_STAGE_CLEAR = _config.get("stage", "music_stage_clear")

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

STARTING_LIVES = _config.getint("game", "starting_lives")
MAX_LIVES = _config.getint("game", "max_lives")
MAX_WEAPONS = _config.getint("game", "max_weapons")
MAX_WEAPON_LEVEL = _config.getint("game", "max_weapon_level")

# Parse weapon names from comma-separated string
_weapon_names_str = _config.get("game", "weapon_names")
WEAPON_NAMES = [name.strip() for name in _weapon_names_str.split(",")]

MAX_SCORE = _config.getint("game", "max_score")
ENEMY_SCORE_NORMAL = _config.getint("game", "enemy_score_normal")
ENEMY_SCORE_BOSS = _config.getint("game", "enemy_score_boss")
PLAYER_SHOT_DAMAGE = _config.getint("game", "player_shot_damage")
BOMB_DAMAGE = _config.getint("game", "bomb_damage")

# ============================================================================
# Graphics Configuration
# ============================================================================

MAX_COLOURS = _config.getint("graphics", "max_colours")

# Parse palette from comma-separated hex values
_palette_str = _config.get("graphics", "palette")
PALETTE = [int(color.strip(), 16) for color in _palette_str.split(",")]
