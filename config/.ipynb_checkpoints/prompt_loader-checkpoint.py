import yaml
from pathlib import Path

PROMPT_FILE = Path("config/prompts.yaml")

_prompts_cache = None


def get_prompt(name: str):
    global _prompts_cache

    if _prompts_cache is None:
        with open(PROMPT_FILE) as f:
            _prompts_cache = yaml.safe_load(f)

    return _prompts_cache.get(name, "")