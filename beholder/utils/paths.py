from pathlib import Path


BASE_DIR = Path(__file__).resolve().parent.parent


def get_data_path(*parts: str) -> Path:
    return BASE_DIR / "data" / Path(*parts)
