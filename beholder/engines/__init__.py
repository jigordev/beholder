from beholder.engines.google import get_google_search_url
from beholder.engines.bing import get_bing_search_url


def get_search_url(engine: str, dork: str) -> str:
    if engine == "google":
        return get_google_search_url(dork)
    elif engine == "bing":
        return get_bing_search_url(dork)
    else:
        raise ValueError(f"Invalid search engine: {engine}")
