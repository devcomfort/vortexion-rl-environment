"""
Player configuration schema.

This module provides a Pydantic schema for player-related configuration constants.
"""

from typing import List

from pydantic import BaseModel, Field, ValidationInfo, field_validator


class PlayerConfigSchema(BaseModel):
    """
    Player configuration schema.

    This schema represents player-related configuration constants including
    initial values and content data. Maximum limits are defined in GameLimitsSchema.

    Parameters
    ----------
    starting_lives : int, optional
        Initial number of lives when starting a new game (1-9). Defaults to 3.
    weapon_names : List[str], optional
        List of weapon names. Length must match the max_weapons value from
        GameLimitsSchema. Defaults to ["A", "B", "C"].

    Examples
    --------
    >>> config = PlayerConfigSchema()
    >>> config.starting_lives
    3
    >>> config.weapon_names
    ['A', 'B', 'C']
    >>> config.model_dump()
    {'starting_lives': 3, 'weapon_names': ['A', 'B', 'C']}
    """

    starting_lives: int = Field(
        default=3,
        ge=1,
        le=9,
        description="Initial number of lives when starting a new game (1-9)",
    )
    weapon_names: List[str] = Field(
        default_factory=lambda: ["A", "B", "C"],
        min_length=1,
        description=(
            "List of weapon names. "
            "Length must match the max_weapons value from GameLimitsSchema."
        ),
    )

    @field_validator("weapon_names")
    @classmethod
    def validate_weapon_names_length(
        cls, v: List[str], info: ValidationInfo
    ) -> List[str]:
        """
        Validate weapon_names is not empty.

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
            If weapon_names is empty.
        """
        if len(v) == 0:
            raise ValueError("weapon_names must have at least one element")
        return v

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
