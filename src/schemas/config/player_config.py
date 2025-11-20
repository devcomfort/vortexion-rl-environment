"""
Player configuration schema.

This module provides a Pydantic schema for player-related configuration constants.
"""

from typing import List

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class PlayerConfigSchema(BaseModel):
    """
    Player configuration schema.

    This schema represents all player-related configuration constants including
    initial values, maximum limits, content data, and damage values.

    Parameters
    ----------
    starting_lives : int, optional
        Initial number of lives when starting a new game (1-9). Defaults to 3.
    max_lives : int, optional
        Maximum number of lives allowed (1-9). Player cannot exceed this limit
        even with power-ups. Defaults to 9.
    max_weapons : int, optional
        Maximum number of weapon types (1-10). Determines the size of weapon
        arrays and UI display. Defaults to 3.
    max_weapon_level : int, optional
        Maximum level for any weapon (1-10). Weapon level cannot exceed this
        value even with power-ups. Defaults to 5.
    weapon_names : List[str], optional
        List of weapon names. Length must match the max_weapons value.
        Defaults to ["A", "B", "C"].
    player_shot_damage : int, optional
        Damage dealt by player shots (1-100). Defaults to 1.
    bomb_damage : int, optional
        Damage dealt by bombs (1-1000). Defaults to 30.

    Examples
    --------
    >>> config = PlayerConfigSchema()
    >>> config.starting_lives
    3
    >>> config.max_lives
    9
    >>> config.weapon_names
    ['A', 'B', 'C']
    >>> config.model_dump()
    {'starting_lives': 3, 'max_lives': 9, 'max_weapons': 3, ...}
    """

    # Initial values
    starting_lives: int = Field(
        default=3,
        ge=1,
        le=9,
        description="Initial number of lives when starting a new game (1-9)",
    )

    # Maximum limits
    max_lives: int = Field(
        default=9,
        ge=1,
        le=9,
        description=(
            "Maximum number of lives allowed (1-9). "
            "Player cannot exceed this limit even with power-ups."
        ),
    )
    max_weapons: int = Field(
        default=3,
        ge=1,
        le=10,
        description=(
            "Maximum number of weapon types (1-10). "
            "Determines the size of weapon arrays and UI display."
        ),
    )
    max_weapon_level: int = Field(
        default=5,
        ge=1,
        le=10,
        description=(
            "Maximum level for any weapon (1-10). "
            "Weapon level cannot exceed this value even with power-ups."
        ),
    )

    # Content data
    weapon_names: List[str] = Field(
        default_factory=lambda: ["A", "B", "C"],
        min_length=1,
        description=("List of weapon names. Length must match the max_weapons value."),
    )

    # Damage values
    player_shot_damage: int = Field(
        default=1,
        ge=1,
        le=100,
        description="Damage dealt by player shots (1-100)",
    )
    bomb_damage: int = Field(
        default=30,
        ge=1,
        le=1000,
        description="Damage dealt by bombs (1-1000)",
    )

    @field_validator("starting_lives")
    @classmethod
    def validate_starting_lives(cls, v: int, info: ValidationInfo) -> int:
        """
        Validate starting_lives doesn't exceed max_lives.

        Parameters
        ----------
        v : int
            Starting lives value to validate.
        info : ValidationInfo
            Validation context containing other field values.

        Returns
        -------
        int
            Validated starting lives.

        Raises
        ------
        ValueError
            If starting_lives exceeds max_lives.
        """
        max_lives = info.data.get("max_lives", 9)
        if v > max_lives:
            raise ValueError(
                f"starting_lives ({v}) cannot exceed max_lives ({max_lives})"
            )
        return v

    @field_validator("weapon_names")
    @classmethod
    def validate_weapon_names_length(
        cls, v: List[str], info: ValidationInfo
    ) -> List[str]:
        """
        Validate weapon_names length matches max_weapons.

        Parameters
        ----------
        v : List[str]
            List of weapon names to validate.
        info : ValidationInfo
            Validation context containing other field values.

        Returns
        -------
        List[str]
            Validated weapon names.

        Raises
        ------
        ValueError
            If weapon_names length doesn't match max_weapons.
        """
        max_weapons = info.data.get("max_weapons", 3)
        if len(v) != max_weapons:
            raise ValueError(
                f"weapon_names must have exactly {max_weapons} elements (matching max_weapons), got {len(v)}"
            )
        return v

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
