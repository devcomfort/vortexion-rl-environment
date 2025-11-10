"""
Entity type schema for serialization.

This module provides a Pydantic schema for EntityType enum serialization.
"""

from pydantic import BaseModel, Field


class EntityTypeSchema(BaseModel):
    """
    Entity type schema for serialization.

    This schema allows EntityType enum values to be serialized to JSON
    and deserialized back to entity type values with validation.

    Parameters
    ----------
    value : int
        The integer value representing the entity type (0-5).

    Examples
    --------
    >>> schema = EntityTypeSchema(value=0)
    >>> schema.value
    0
    >>> schema.model_dump()
    {'value': 0}
    """

    value: int = Field(ge=0, le=5, description="Entity type value (0-5)")

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable

