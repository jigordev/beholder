import urllib.parse


GOOGLE_BASE_URL = "https://google.com"


def get_google_search_url(dork):
    dork = urllib.parse.quote_plus(dork)
    return f"{GOOGLE_BASE_URL}/search?q={dork}"
