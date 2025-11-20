"""Tilemap resource file paths schema.

This module provides a Pydantic schema for tilemap resource file paths.
"""

from typing import Dict

from pydantic import BaseModel, Field


class TilemapResourcesSchema(BaseModel):
    """
    Tilemap resource file paths schema.

    This schema represents all tilemap resource file paths used in the game.

    Parameters
    ----------
    title : str, optional
        Title screen tilemap file path. Defaults to "title.tmx".
    complete : str, optional
        Game complete screen tilemap file path. Defaults to "complete.tmx".
    stage_files : Dict[int, str], optional
        Dictionary mapping stage numbers to tilemap file paths.
        Defaults to stage 1-5 mappings.

    Examples
    --------
    >>> tilemaps = TilemapResourcesSchema()
    >>> tilemaps.title
    'title.tmx'
    >>> tilemaps.stage_files[1]
    'stage_1.tmx'
    >>> tilemaps.model_dump()
    {'title': 'title.tmx', 'complete': 'complete.tmx', 'stage_files': {...}}
    """

    title: str = Field(
        default="title.tmx",
        description="Title screen tilemap file path",
    )
    complete: str = Field(
        default="complete.tmx",
        description="Game complete screen tilemap file path",
    )
    stage_files: Dict[int, str] = Field(
        default_factory=lambda: {
            1: "stage_1.tmx",
            2: "stage_2.tmx",
            3: "stage_3.tmx",
            4: "stage_4.tmx",
            5: "stage_5.tmx",
        },
        description="Dictionary mapping stage numbers to tilemap file paths",
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
