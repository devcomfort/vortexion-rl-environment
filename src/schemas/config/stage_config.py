"""
Stage configuration schema.

This module provides a Pydantic schema for stage-related configuration constants.
Note: Resource file paths (music, tilemaps) are defined in resources/ module.
"""

from pydantic import BaseModel, Field

from ..state.stage import StageSchema


class StageConfigSchema(BaseModel):
    """
    Stage configuration schema.

    This schema represents stage-related configuration for game logic.
    Resource file paths (music files, tilemap files) are defined separately
    in the resources/ module.

    Parameters
    ----------
    final_stage : StageSchema, optional
        Final stage number. Game progression ends after completing this stage.
        Used for stage progression checks and game completion logic.
        Defaults to StageSchema(stage=5).

    Examples
    --------
    >>> config = StageConfigSchema()
    >>> config.final_stage.stage
    5
    >>> config.model_dump()
    {'final_stage': {'stage': 5}}
    """

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
