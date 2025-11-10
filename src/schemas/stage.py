"""
Stage number schema for serialization.

This module provides a Pydantic schema for stage number serialization.
"""

from pydantic import BaseModel, Field


class StageSchema(BaseModel):
    """
    Stage number schema for serialization.

    This schema allows stage numbers to be serialized to JSON
    and deserialized back to stage numbers with validation.

    Parameters
    ----------
    stage : int
        The integer value representing the stage number (1-5).

    Examples
    --------
    >>> schema = StageSchema(stage=1)
    >>> schema.stage
    1
    >>> schema.model_dump()
    {'stage': 1}
    """

    stage: int = Field(ge=1, le=5, description="Stage number (1-5)")

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
