"""
Application configuration schema.

This module provides a Pydantic schema for application configuration constants.
"""

from pydantic import BaseModel, Field


class AppConfigSchema(BaseModel):
    """
    Application configuration schema.

    This schema represents all application-level configuration constants
    including window settings, FPS, and display scaling.

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
        Display scaling factor for window rendering (1-8). Controls the
        pixel-perfect scaling of the game window on screen. Higher values
        result in larger window size. Example: 2 means 256x192 game resolution
        is displayed as 512x384 pixels. Defaults to 2.
    capture_scale : int, optional
        Capture scaling factor for screenshots/recordings (1-8). Controls the
        resolution of captured images/videos independent of display. Useful for
        high-quality captures without affecting gameplay window size. Example:
        4 means screenshots are saved at 1024x768 resolution even if
        display_scale=2. Defaults to 2.

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
        default=2,
        ge=1,
        le=8,
        description=(
            "Display scaling factor for window rendering (1-8). "
            "Controls the pixel-perfect scaling of the game window on screen. "
            "Higher values result in larger window size. "
            "Example: 2 means 256x192 game resolution is displayed as 512x384 pixels."
        ),
    )
    capture_scale: int = Field(
        default=2,
        ge=1,
        le=8,
        description=(
            "Capture scaling factor for screenshots/recordings (1-8). "
            "Controls the resolution of captured images/videos independent of display. "
            "Useful for high-quality captures without affecting gameplay window size. "
            "Example: 4 means screenshots are saved at 1024x768 resolution even if display_scale=2."
        ),
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
