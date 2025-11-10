"""
Graphics configuration schema.

This module provides a Pydantic schema for graphics configuration constants.
"""

from typing import List

from pydantic import BaseModel, Field, field_validator


class GraphicsConfigSchema(BaseModel):
    """
    Graphics configuration schema.

    This schema represents graphics-related configuration including
    color palette and maximum colors.

    Parameters
    ----------
    max_colours : int, optional
        Maximum number of colors in palette (1-256). Defaults to 16.
    palette : List[int], optional
        Color palette as list of RGB hex values. Defaults to 16-color palette.
        Each value should be a valid 24-bit RGB color (0x000000-0xFFFFFF).

    Examples
    --------
    >>> config = GraphicsConfigSchema()
    >>> config.max_colours
    16
    >>> len(config.palette)
    16
    >>> config.model_dump()
    {'max_colours': 16, 'palette': [16711935, 0, ...]}
    """

    max_colours: int = Field(
        default=16,
        ge=1,
        le=256,
        description="Maximum number of colors in palette (1-256)",
    )
    palette: List[int] = Field(
        default_factory=lambda: [
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
        ],
        description="Color palette as list of RGB hex values",
    )

    @field_validator("palette")
    @classmethod
    def validate_palette(cls, v: List[int]) -> List[int]:
        """
        Validate palette colors are within valid range.

        Parameters
        ----------
        v : List[int]
            List of color values to validate.

        Returns
        -------
        List[int]
            Validated color values.

        Raises
        ------
        ValueError
            If any color value is outside the valid range (0x000000-0xFFFFFF).
        """
        for color in v:
            if not (0x000000 <= color <= 0xFFFFFF):
                raise ValueError(
                    f"palette color must be between 0x000000 and 0xFFFFFF, got 0x{color:X}"
                )
        return v

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
