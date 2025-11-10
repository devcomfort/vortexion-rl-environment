"""
Entity configuration loader using JSONL format.

This module loads entity-specific configuration values from a JSONL file,
allowing easy adjustment of game mechanics like speeds, delays, and other
entity parameters without modifying code.
"""

import json
from pathlib import Path
from typing import Any, Dict, Optional

# Configuration file path (project root / working directory)
# Try project root first, then fallback to src/ for packaging
CONFIG_FILE_ROOT = Path(__file__).parent.parent / "entity_config.jsonl"
CONFIG_FILE_PACKAGED = Path(__file__).parent / "entity_config.jsonl"

# Global configuration cache
_config_cache: Optional[Dict[str, Dict[str, Any]]] = None


def _load_config() -> Dict[str, Dict[str, Any]]:
    """Load entity configuration from JSONL file."""
    global _config_cache
    
    if _config_cache is not None:
        return _config_cache
    
    # Try project root first, then fallback to packaged location
    config_file = None
    if CONFIG_FILE_ROOT.exists():
        config_file = CONFIG_FILE_ROOT
    elif CONFIG_FILE_PACKAGED.exists():
        config_file = CONFIG_FILE_PACKAGED
    else:
        raise FileNotFoundError(
            f"Entity configuration file not found. Tried: {CONFIG_FILE_ROOT} and {CONFIG_FILE_PACKAGED}"
        )
    
    config_dict = {}
    with open(config_file, "r", encoding="utf-8") as f:
        for line in f:
            line = line.strip()
            if not line:
                continue
            entity_config = json.loads(line)
            entity_type = entity_config.pop("type")
            config_dict[entity_type] = entity_config
    
    _config_cache = config_dict
    return config_dict


def get(entity_type: str, key: str, default: Any = None) -> Any:
    """
    Get a configuration value for a specific entity type.
    
    Parameters
    ----------
    entity_type : str
        The entity type (e.g., "enemy_a", "player", "player_shot")
    key : str
        The configuration key (e.g., "speed", "bullet_speed")
    default : Any, optional
        Default value if key is not found (default: None)
    
    Returns
    -------
    Any
        The configuration value, or default if not found
    
    Examples
    --------
    >>> speed = get("enemy_a", "speed", 1.0)
    >>> bullet_speed = get("enemy_a", "bullet_speed", 2.0)
    """
    config = _load_config()
    entity_config = config.get(entity_type, {})
    return entity_config.get(key, default)


def get_all(entity_type: str) -> Dict[str, Any]:
    """
    Get all configuration values for a specific entity type.
    
    Parameters
    ----------
    entity_type : str
        The entity type (e.g., "enemy_a", "player")
    
    Returns
    -------
    Dict[str, Any]
        Dictionary containing all configuration values for the entity type
    
    Examples
    --------
    >>> enemy_a_config = get_all("enemy_a")
    >>> speed = enemy_a_config.get("speed", 1.0)
    """
    config = _load_config()
    return config.get(entity_type, {}).copy()


def reload():
    """Reload configuration from file (clears cache)."""
    global _config_cache
    _config_cache = None
    _load_config()

