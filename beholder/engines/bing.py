import urllib.parse

BING_BASE_URL = "https://www.bing.com"


def get_bing_search_url(dork):
    dork = urllib.parse.quote_plus(dork)
    return f"{BING_BASE_URL}/search?q={dork}"
