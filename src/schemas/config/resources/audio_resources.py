"""Audio resource file paths schema.

This module provides a Pydantic schema for audio resource file paths.
"""

from typing import Dict

from pydantic import BaseModel, Field


class AudioResourcesSchema(BaseModel):
    """
    Audio resource file paths schema.

    This schema represents all audio resource file paths including
    sound effects and music files.

    Parameters
    ----------
    sound_effects_file : str, optional
        Sound effects resource file path (Pyxel format). Defaults to "sounds.pyxres".
    music_title : str, optional
        Title screen music file path. Defaults to "music_title.json".
    music_stage_files : Dict[int, str], optional
        Dictionary mapping stage numbers to music file paths.
        Defaults to stage 1-5 mappings.
    music_game_complete : str, optional
        Game complete music file path. Defaults to "music_game_complete.json".
    music_game_over : str, optional
        Game over music file path. Defaults to "music_game_over.json".
    music_boss : str, optional
        Boss battle music file path. Defaults to "music_boss.json".
    music_stage_clear : str, optional
        Stage clear music file path. Defaults to "music_stage_clear.json".

    Examples
    --------
    >>> audio = AudioResourcesSchema()
    >>> audio.sound_effects_file
    'sounds.pyxres'
    >>> audio.music_title
    'music_title.json'
    >>> audio.model_dump()
    {'sound_effects_file': 'sounds.pyxres', 'music_title': 'music_title.json', ...}
    """

    sound_effects_file: str = Field(
        default="sounds.pyxres",
        description="Sound effects resource file path (Pyxel format)",
    )
    music_title: str = Field(
        default="music_title.json",
        description="Title screen music file path",
    )
    music_stage_files: Dict[int, str] = Field(
        default_factory=lambda: {
            1: "music_stage_1.json",
            2: "music_vortex.json",
            3: "music_stage_3.json",
            4: "music_vortex.json",
            5: "music_stage_5.json",
        },
        description="Dictionary mapping stage numbers to music file paths",
    )
    music_game_complete: str = Field(
        default="music_game_complete.json",
        description="Game complete music file path",
    )
    music_game_over: str = Field(
        default="music_game_over.json",
        description="Game over music file path",
    )
    music_boss: str = Field(
        default="music_boss.json",
        description="Boss battle music file path",
    )
    music_stage_clear: str = Field(
        default="music_stage_clear.json",
        description="Stage clear music file path",
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable
