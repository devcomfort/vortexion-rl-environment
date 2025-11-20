"""Map resource file paths schema.

This module provides a Pydantic schema for map resource file paths
and stage progression configuration.
"""

from typing import Dict

from pydantic import BaseModel, Field


class MapResourcesSchema(BaseModel):
    """
    Map resource file paths schema.

    This schema represents all map resource file paths used in the game
    and stage progression configuration.

    Parameters
    ----------
    title : str, optional
        Title screen map file path. Defaults to "title.tmx".
    complete : str, optional
        Game complete screen map file path. Defaults to "complete.tmx".
    stage_files : Dict[int, str], optional
        Dictionary mapping stage numbers to map file paths.
        Defaults to stage 1-5 mappings.
    final_stage : int, optional
        Final stage number (1-5). Game progression ends after completing this stage.
        Used for stage progression checks and game completion logic.
        Defaults to 5.

    Examples
    --------
    >>> maps = MapResourcesSchema()
    >>> maps.title
    'title.tmx'
    >>> maps.stage_files[1]
    'stage_1.tmx'
    >>> maps.final_stage
    5
    >>> maps.model_dump()
    {'title': 'title.tmx', 'complete': 'complete.tmx', 'stage_files': {...}, 'final_stage': {...}}
    """

    title: str = Field(
        default="title.tmx",
        description="Title screen map file path",
    )
    complete: str = Field(
        default="complete.tmx",
        description="Game complete screen map file path",
    )
    stage_files: Dict[int, str] = Field(
        default_factory=lambda: {
            1: "stage_1.tmx",
            2: "stage_2.tmx",
            3: "stage_3.tmx",
            4: "stage_4.tmx",
            5: "stage_5.tmx",
        },
        description="Dictionary mapping stage numbers to map file paths",
    )
    final_stage: int = Field(
        default=5,
        ge=1,
        le=5,
        description=(
            "Final stage number (1-5). "
            "Game progression ends after completing this stage. "
            "Used for stage progression checks and game completion logic."
        ),
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
