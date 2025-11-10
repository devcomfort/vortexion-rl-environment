"""
Game configuration constants schema.

This module provides a Pydantic schema for game configuration constants.
"""

from typing import List

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class GameConfigSchema(BaseModel):
    """
    Game configuration constants schema.

    This schema represents all game configuration constants that can be
    serialized and potentially modified with validation.

    Parameters
    ----------
    starting_lives : int, optional
        Initial number of lives when starting a new game (1-9). Defaults to 3.
    max_lives : int, optional
        Maximum number of lives allowed (1-9). Defaults to 9.
    max_weapons : int, optional
        Maximum number of weapons (1-10). Defaults to 3.
    max_weapon_level : int, optional
        Maximum level for any weapon (1-10). Defaults to 5.
    max_score : int, optional
        Maximum score cap (1-9999999). Defaults to 999999.
    weapon_names : List[str], optional
        List of weapon names (length must match max_weapons). Defaults to ["A", "B", "C"].

    Examples
    --------
    >>> config = GameConfigSchema()
    >>> config.starting_lives
    3
    >>> config.max_score
    999999
    >>> config.model_dump()
    {'starting_lives': 3, 'max_lives': 9, ...}
    """

    starting_lives: int = Field(
        default=3,
        ge=1,
        le=9,
        description="Initial number of lives when starting a new game (1-9)",
    )
    max_lives: int = Field(
        default=9, ge=1, le=9, description="Maximum number of lives allowed (1-9)"
    )
    max_weapons: int = Field(
        default=3, ge=1, le=10, description="Maximum number of weapons (1-10)"
    )
    max_weapon_level: int = Field(
        default=5, ge=1, le=10, description="Maximum level for any weapon (1-10)"
    )
    max_score: int = Field(
        default=999999, ge=1, le=9999999, description="Maximum score cap (1-9999999)"
    )
    weapon_names: List[str] = Field(
        default_factory=lambda: ["A", "B", "C"],
        min_length=1,
        description="List of weapon names",
    )

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

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
