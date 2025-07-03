import json
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent


def get_data_path(*parts: str) -> Path:
    return BASE_DIR / "data" / Path(*parts)


def load_dorks_file(filename: str) -> dict:
    with open(filename) as dorks_file:
        return json.load(dorks_file)


def load_dorks_template(engine: str, filename: str) -> dict:
    template_file = get_data_path("templates", engine, filename)
    return load_dorks_file(template_file)
