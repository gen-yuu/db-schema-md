import json
from pathlib import Path
from typing import Any, Dict

def load_config(path: Path) -> Dict[str, Any]:
    """
    Load JSON config for database connection (and any other settings).

    Expected keys in the JSON:
      - DB_HOST
      - DB_USER
      - DB_PASSWORD
      - DB_PORT
      - DB_NAME
    """
    if not path.exists():
        raise FileNotFoundError(f"Config file not found: {path}")

    with path.open(encoding="utf-8") as f:
        cfg = json.load(f)

    # 必要なキーが揃っているか確認
    required = {"DB_HOST", "DB_USER", "DB_PASSWORD", "DB_PORT", "DB_NAME"}
    missing = required - cfg.keys()
    if missing:
        raise KeyError(f"Missing config keys: {missing}")

    return cfg