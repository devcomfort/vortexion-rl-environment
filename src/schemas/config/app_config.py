"""
Application configuration schema.

This module provides a Pydantic schema for application configuration constants.
"""

from pydantic import BaseModel, Field


class AppConfigSchema(BaseModel):
    """
    Application configuration schema.

    This schema represents all application-level configuration constants
    including window settings, FPS, and resource file paths.

    Parameters
    ----------
    version : str, optional
        Application version string. Defaults to "1.0".
    width : int, optional
        Window width in pixels (1-4096). Defaults to 256.
    height : int, optional
        Window height in pixels (1-4096). Defaults to 192.
    name : str, optional
        Application name. Defaults to "VORTEXION".
    fps : int, optional
        Frames per second (1-120). Defaults to 60.
    display_scale : int, optional
        Display scaling factor (1-8). Defaults to 2.
    capture_scale : int, optional
        Capture scaling factor (1-8). Defaults to 2.
    gfx_file : str, optional
        Graphics resource file path. Defaults to "gfx.png".
    sounds_res_file : str, optional
        Sounds resource file path. Defaults to "sounds.pyxres".

    Examples
    --------
    >>> config = AppConfigSchema()
    >>> config.width
    256
    >>> config.fps
    60
    >>> config.model_dump()
    {'version': '1.0', 'width': 256, ...}
    """

    version: str = Field(default="1.0", description="Application version string")
    width: int = Field(
        default=256, ge=1, le=4096, description="Window width in pixels (1-4096)"
    )
    height: int = Field(
        default=192, ge=1, le=4096, description="Window height in pixels (1-4096)"
    )
    name: str = Field(default="VORTEXION", description="Application name")
    fps: int = Field(default=60, ge=1, le=120, description="Frames per second (1-120)")
    display_scale: int = Field(
        default=2, ge=1, le=8, description="Display scaling factor (1-8)"
    )
    capture_scale: int = Field(
        default=2, ge=1, le=8, description="Capture scaling factor (1-8)"
    )
    gfx_file: str = Field(default="gfx.png", description="Graphics resource file path")
    sounds_res_file: str = Field(
        default="sounds.pyxres", description="Sounds resource file path"
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
