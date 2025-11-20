"""Game progression limits configuration schema.

This module provides a Pydantic schema for game progression limits.
"""

from pydantic import BaseModel, Field

from ...state.stage import StageSchema


class ProgressionLimitsSchema(BaseModel):
    """
    Game progression limits schema.

    This schema represents limits related to game progression.

    Parameters
    ----------
    final_stage : StageSchema, optional
        Final stage number. Game progression ends after completing this stage.
        Used for stage progression checks and game completion logic.
        Defaults to StageSchema(stage=5).

    Examples
    --------
    >>> progression = ProgressionLimitsSchema()
    >>> progression.final_stage.stage
    5
    >>> progression.model_dump()
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
