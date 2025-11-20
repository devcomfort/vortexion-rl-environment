"""Tilemap resource file paths schema.

This module provides a Pydantic schema for tilemap resource file paths
and stage progression configuration.
"""

from typing import Dict

from pydantic import BaseModel, Field

from ...state.stage import StageSchema


class TilemapResourcesSchema(BaseModel):
    """
    Tilemap resource file paths schema.

    This schema represents all tilemap resource file paths used in the game
    and stage progression configuration.

    Parameters
    ----------
    title : str, optional
        Title screen tilemap file path. Defaults to "title.tmx".
    complete : str, optional
        Game complete screen tilemap file path. Defaults to "complete.tmx".
    stage_files : Dict[int, str], optional
        Dictionary mapping stage numbers to tilemap file paths.
        Defaults to stage 1-5 mappings.
    final_stage : StageSchema, optional
        Final stage number. Game progression ends after completing this stage.
        Used for stage progression checks and game completion logic.
        Defaults to StageSchema(stage=5).

    Examples
    --------
    >>> tilemaps = TilemapResourcesSchema()
    >>> tilemaps.title
    'title.tmx'
    >>> tilemaps.stage_files[1]
    'stage_1.tmx'
    >>> tilemaps.final_stage.stage
    5
    >>> tilemaps.model_dump()
    {'title': 'title.tmx', 'complete': 'complete.tmx', 'stage_files': {...}, 'final_stage': {...}}
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
    final_stage: StageSchema = Field(
        default_factory=lambda: StageSchema(stage=5),
        description=(
            "Final stage number. "
            "Game progression ends after completing this stage. "
            "Used for stage progression checks and game completion logic."
        ),
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
