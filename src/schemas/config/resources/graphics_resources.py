"""Graphics resource file paths schema.

This module provides a Pydantic schema for graphics resource file paths.
"""

from pydantic import BaseModel, Field


class GraphicsResourcesSchema(BaseModel):
    """
    Graphics resource file paths schema.

    This schema represents all graphics resource file paths used in the game.

    Parameters
    ----------
    image_file : str, optional
        Main graphics image file path (PNG format). Defaults to "gfx.png".

    Examples
    --------
    >>> graphics = GraphicsResourcesSchema()
    >>> graphics.image_file
    'gfx.png'
    >>> graphics.model_dump()
    {'image_file': 'gfx.png'}
    """

    image_file: str = Field(
        default="gfx.png",
        description="Main graphics image file path (PNG format)",
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
