"""Resource file path schemas.

This module provides schemas for organizing all game resource file paths
by type (graphics, audio, tilemaps).
"""

from .audio_resources import AudioResourcesSchema
from .graphics_resources import GraphicsResourcesSchema
from .tilemap_resources import TilemapResourcesSchema

__all__ = [
    "GraphicsResourcesSchema",
    "AudioResourcesSchema",
    "TilemapResourcesSchema",
]
