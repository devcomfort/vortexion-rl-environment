"""
Stage configuration schema.

This module provides a Pydantic schema for stage-related configuration constants.
Note: Resource file paths (music, tilemaps) are defined in resources/ module.
"""

from pydantic import BaseModel


class StageConfigSchema(BaseModel):
    """
    Stage configuration schema.

    This schema represents stage-related configuration for game logic.
    Resource file paths (music files, tilemap files) are defined separately
    in the resources/ module.

    Note: This schema is currently minimal as most stage-related settings
    have been moved to more appropriate modules:
    - final_stage -> GameLimitsSchema.progression.final_stage
    - music files -> AudioResourcesSchema
    - tilemap files -> TilemapResourcesSchema

    Examples
    --------
    >>> config = StageConfigSchema()
    >>> config.model_dump()
    {}
    """

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
