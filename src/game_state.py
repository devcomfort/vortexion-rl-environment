from dataclasses import dataclass, field
from typing import Callable, List

import numpy as np

from const import (
    STARTING_LIVES,
    MAX_WEAPONS,
    MAX_SCORE,
    MAX_WEAPON_LEVEL,
    MAX_LIVES,
    StageNum,
    FINAL_STAGE,
)


@dataclass
class GameState:
    """
    Game state management using dataclass for type safety and validation.

    This class manages all game variables including score, lives, weapons,
    and stage progression. It implements an observer pattern for reactive
    state management, allowing components to subscribe to state changes.
    """

    score: int = 0
    high_score: int = 0
    selected_weapon: int = 0
    lives: int = STARTING_LIVES
    weapon_levels: List[int] = field(default_factory=lambda: [0] * MAX_WEAPONS)
    current_stage: StageNum = StageNum.STAGE_1

    # Private attributes not part of dataclass fields
    _game: object = field(default=None, init=False, repr=False)
    _observers: List[Callable[[str, object], None]] = field(
        default_factory=list, init=False, repr=False
    )

    def __init__(self, game=None, **kwargs):
        """
        Initialize GameState with optional game reference.

        Args:
            game: Optional game instance reference
            **kwargs: Field values for dataclass fields
        """
        # Set default values for fields not provided
        if "score" not in kwargs:
            kwargs["score"] = 0
        if "high_score" not in kwargs:
            kwargs["high_score"] = 0
        if "selected_weapon" not in kwargs:
            kwargs["selected_weapon"] = 0
        if "lives" not in kwargs:
            kwargs["lives"] = STARTING_LIVES
        if "weapon_levels" not in kwargs:
            kwargs["weapon_levels"] = [0] * MAX_WEAPONS
        if "current_stage" not in kwargs:
            kwargs["current_stage"] = StageNum.STAGE_1

        # Initialize dataclass fields manually
        self.score = kwargs["score"]
        self.high_score = kwargs["high_score"]
        self.selected_weapon = kwargs["selected_weapon"]
        self.lives = kwargs["lives"]
        self.weapon_levels = kwargs["weapon_levels"]
        self.current_stage = kwargs["current_stage"]

        # Set private attributes
        self._game = game
        self._observers = []

        # Validate and normalize field values
        self.__post_init__()

    def __post_init__(self):
        """Validate and normalize field values after initialization."""
        # Validate and clamp score
        self.score = int(np.clip(self.score, 0, MAX_SCORE))
        self.high_score = int(np.clip(self.high_score, 0, MAX_SCORE))

        # Validate and clamp lives
        self.lives = int(np.clip(self.lives, 0, MAX_LIVES))

        # Validate weapon_levels length and values
        if len(self.weapon_levels) != MAX_WEAPONS:
            self.weapon_levels = [0] * MAX_WEAPONS
        self.weapon_levels = [
            int(np.clip(level, 0, MAX_WEAPON_LEVEL)) for level in self.weapon_levels
        ]

        # Validate selected_weapon index
        if not (0 <= self.selected_weapon < MAX_WEAPONS):
            self.selected_weapon = 0
        if self.selected_weapon >= len(self.weapon_levels):
            self.selected_weapon = 0

    def subscribe(self, callback: Callable[[str, object], None]):
        """
        Subscribe to state changes.

        Args:
            callback: Function that receives (field_name, new_value) when state changes
        """
        self._observers.append(callback)

    def unsubscribe(self, callback: Callable[[str, object], None]):
        """Unsubscribe from state changes."""
        if callback in self._observers:
            self._observers.remove(callback)

    def _notify(self, field_name: str, value: object):
        """Notify all observers of a state change."""
        for observer in self._observers:
            try:
                observer(field_name, value)
            except Exception:
                # Don't let observer errors break the game
                pass

    def is_vortex_stage(self) -> bool:
        """Check if current stage is a vortex stage."""
        return self.current_stage % 2 == 0

    def new_game(self):
        """Reset game state for a new game."""
        self.continue_game()
        self.current_stage = StageNum.STAGE_1
        self._notify("current_stage", self.current_stage)

    def continue_game(self):
        """Reset game state for continuing."""
        self.score = 0
        self.selected_weapon = 0
        self.weapon_levels = [0] * MAX_WEAPONS
        self.lives = STARTING_LIVES
        self._notify("score", self.score)
        self._notify("selected_weapon", self.selected_weapon)
        self._notify("weapon_levels", self.weapon_levels)
        self._notify("lives", self.lives)

    def go_to_next_stage(self) -> bool:
        """Advance to the next stage. Returns True if successful."""
        if self.current_stage < FINAL_STAGE:
            self.current_stage = StageNum(self.current_stage + 1)
            self._notify("current_stage", self.current_stage)
            return True
        return False

    def add_life(self):
        """Add one life, respecting maximum limit."""
        old_lives = self.lives
        self.lives = int(np.clip(self.lives + 1, 0, MAX_LIVES))
        if self.lives != old_lives:
            self._notify("lives", self.lives)

    def subtract_life(self):
        """Subtract one life, respecting minimum limit."""
        old_lives = self.lives
        self.lives = int(np.clip(self.lives - 1, 0, MAX_LIVES))
        if self.lives != old_lives:
            self._notify("lives", self.lives)

    def add_score(self, amount: int):
        """Add score and update high score if necessary."""
        old_score = self.score
        old_high_score = self.high_score
        self.score = int(np.clip(self.score + amount, 0, MAX_SCORE))
        self.high_score = max(self.score, self.high_score)
        if self.score != old_score:
            self._notify("score", self.score)
        if self.high_score != old_high_score:
            self._notify("high_score", self.high_score)

    def decrease_all_weapon_levels(self, amount: int):
        """Decrease all weapon levels by specified amount."""
        changed = False
        for i in range(len(self.weapon_levels)):
            old_level = self.weapon_levels[i]
            self.weapon_levels[i] = int(
                np.clip(self.weapon_levels[i] - amount, 0, MAX_WEAPON_LEVEL)
            )
            if self.weapon_levels[i] != old_level:
                changed = True
        if changed:
            self._notify("weapon_levels", self.weapon_levels)

    def increase_all_weapon_levels(self, amount: int):
        """Increase all weapon levels by specified amount."""
        changed = False
        for i in range(len(self.weapon_levels)):
            old_level = self.weapon_levels[i]
            self.weapon_levels[i] = int(
                np.clip(self.weapon_levels[i] + amount, 0, MAX_WEAPON_LEVEL)
            )
            if self.weapon_levels[i] != old_level:
                changed = True
        if changed:
            self._notify("weapon_levels", self.weapon_levels)

    def change_weapon(self, weapon_index: int):
        """Change to a different weapon."""
        if 0 <= weapon_index < MAX_WEAPONS:
            old_weapon = self.selected_weapon
            self.selected_weapon = weapon_index
            if self.selected_weapon != old_weapon:
                self._notify("selected_weapon", self.selected_weapon)

    def add_current_weapon_level(self):
        """Increase the current weapon's level."""
        old_level = self.weapon_levels[self.selected_weapon]
        self.weapon_levels[self.selected_weapon] = int(
            np.clip(self.weapon_levels[self.selected_weapon] + 1, 0, MAX_WEAPON_LEVEL)
        )
        if self.weapon_levels[self.selected_weapon] != old_level:
            self._notify("weapon_levels", self.weapon_levels)
