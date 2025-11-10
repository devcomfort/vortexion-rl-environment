"""
Stage configuration schema.

This module provides a Pydantic schema for stage-related configuration constants.
"""

from typing import Dict

from pydantic import BaseModel, Field

from .stage import StageSchema


class StageConfigSchema(BaseModel):
    """
    Stage configuration schema.

    This schema represents stage-related configuration including
    music files and final stage information.

    Parameters
    ----------
    final_stage : StageSchema, optional
        Final stage number. Defaults to StageSchema(stage=5).
    stage_music_files : Dict[int, str], optional
        Dictionary mapping stage numbers to music file paths.
        Defaults to stage 1-5 mappings.
    music_game_complete : str, optional
        Game complete music file path. Defaults to "music_game_complete.json".
    music_game_over : str, optional
        Game over music file path. Defaults to "music_game_over.json".
    music_boss : str, optional
        Boss music file path. Defaults to "music_boss.json".
    music_stage_clear : str, optional
        Stage clear music file path. Defaults to "music_stage_clear.json".

    Examples
    --------
    >>> config = StageConfigSchema()
    >>> config.final_stage.stage
    5
    >>> config.music_game_complete
    'music_game_complete.json'
    >>> config.model_dump()
    {'final_stage': {'stage': 5}, 'stage_music_files': {...}, ...}
    """

    final_stage: StageSchema = Field(
        default_factory=lambda: StageSchema(stage=5),
        description="Final stage number",
    )
    stage_music_files: Dict[int, str] = Field(
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
        default="music_game_over.json", description="Game over music file path"
    )
    music_boss: str = Field(default="music_boss.json", description="Boss music file path")
    music_stage_clear: str = Field(
        default="music_stage_clear.json", description="Stage clear music file path"
    )

    class Config:
        """Pydantic configuration."""

        frozen = True  # Make schema immutable

