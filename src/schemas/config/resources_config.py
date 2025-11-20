"""Resources configuration schema.

This module provides a unified schema for all resource file paths.
"""

from pydantic import BaseModel, Field

from .resources import (
    AudioResourcesSchema,
    GraphicsResourcesSchema,
    MapResourcesSchema,
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
    maps : MapResourcesSchema, optional
        Map resource file paths. Defaults to MapResourcesSchema().

    Examples
    --------
    >>> resources = ResourcesConfigSchema()
    >>> resources.graphics.image_file
    'gfx.png'
    >>> resources.audio.music_title
    'music_title.json'
    >>> resources.maps.title
    'title.tmx'
    >>> resources.model_dump()
    {'graphics': {'image_file': 'gfx.png'}, 'audio': {...}, 'maps': {...}}
    """

    graphics: GraphicsResourcesSchema = Field(
        default_factory=GraphicsResourcesSchema,
        description="Graphics resource file paths",
    )
    audio: AudioResourcesSchema = Field(
        default_factory=AudioResourcesSchema,
        description="Audio resource file paths",
    )
    maps: MapResourcesSchema = Field(
        default_factory=MapResourcesSchema,
        description="Map resource file paths",
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
