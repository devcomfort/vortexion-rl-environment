"""Resources configuration schema.

This module provides a unified schema for all resource file paths.
"""

from pydantic import BaseModel, Field

from .resources import (
    AudioResourcesSchema,
    GraphicsResourcesSchema,
    TilemapResourcesSchema,
)


class ResourcesConfigSchema(BaseModel):
    """
    Resources configuration schema.

    This schema centralizes all resource file paths organized by type.

    Parameters
    ----------
    graphics : GraphicsResourcesSchema, optional
        Graphics resource file paths. Defaults to GraphicsResourcesSchema().
    audio : AudioResourcesSchema, optional
        Audio resource file paths. Defaults to AudioResourcesSchema().
    tilemaps : TilemapResourcesSchema, optional
        Tilemap resource file paths. Defaults to TilemapResourcesSchema().

    Examples
    --------
    >>> resources = ResourcesConfigSchema()
    >>> resources.graphics.image_file
    'gfx.png'
    >>> resources.audio.music_title
    'music_title.json'
    >>> resources.tilemaps.title
    'title.tmx'
    >>> resources.model_dump()
    {'graphics': {'image_file': 'gfx.png'}, 'audio': {...}, 'tilemaps': {...}}
    """

    graphics: GraphicsResourcesSchema = Field(
        default_factory=GraphicsResourcesSchema,
        description="Graphics resource file paths",
    )
    audio: AudioResourcesSchema = Field(
        default_factory=AudioResourcesSchema,
        description="Audio resource file paths",
    )
    tilemaps: TilemapResourcesSchema = Field(
        default_factory=TilemapResourcesSchema,
        description="Tilemap resource file paths",
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
