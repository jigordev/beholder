import urllib.parse
from beholder.utils.paths import load_dorks_file, load_dorks_template
from beholder.engines import BaseDorksEngine
from beholder.utils.parse import parse_query


BING_BASE_URL = "https://www.bing.com"


class BingDorksEngine(BaseDorksEngine):
    def site(self, args: list[str]):
        self._make_query_by_args("site", args)
        return self

    def domain(self, args: list[str]):
        self._make_query_by_args("domain", args)
        return self

    def url(self, args: list[str]):
        self._make_query_by_args("url", args)
        return self

    def inbody(self, args: list[str]):
        self._make_query_by_args("inbody", args)
        return self

    def intitle(self, args: list[str]):
        self._make_query_by_args("intitle", args)
        return self

    def inurl(self, args: list[str]):
        self._make_query_by_args("inurl", args)
        return self

    def ext(self, args: list[str]):
        self._make_query_by_args("ext", args)
        return self

    def filetype(self, args: list[str]):
        self._make_query_by_args("filetype", args)
        return self

    def terms(self, args: list[str]):
        query = [f'"{i}"' for i in args]
        query = " ".join(query)
        self.dork += f" {query}"
        return self

    def exclude(self, args: list[str]):
        query = [f"-{i}" for i in args]
        query = " ".join(query)
        self.dork += f" {query}"
        return self

    def _build_url(self):
        query = urllib.parse.quote_plus(self.dork)
        self.search_url = f"{BING_BASE_URL}/search?q={query}"


def search_bing_dorks(
    query: str = None,
    quoted_terms: list[str] = None,
    sites: list[str] = None,
    domains: list[str] = None,
    files: list[str] = None,
    titles: list[str] = None,
    texts: list[str] = None,
    urls: list[str] = None,
    excludes: list[str] = None,
    template: str = None,
    template_file: str = None,
):
    quoted_terms = quoted_terms or []
    sites = sites or []
    files = files or []
    titles = titles or []
    texts = texts or []
    urls = urls or []
    excludes = excludes or []

    dorks_data = {}
    if template:
        dorks_data = load_dorks_template("bing", template)
    elif template_file:
        dorks_data = load_dorks_file(template_file)

    if dorks_data:
        dorks_data = parse_query(dorks_data, query)

    engine = BingDorksEngine()
    engine.terms([query])
    engine.terms(quoted_terms or dorks_data.get("quoted_terms", []))
    engine.site(sites or dorks_data.get("site", []))
    engine.domain(domains or dorks_data.get("domain", []))
    engine.filetype(files or dorks_data.get("filetype", []))
    engine.intitle(titles or dorks_data.get("intitle", []))
    engine.inbody(texts or dorks_data.get("inbody", []))
    engine.inurl(urls or dorks_data.get("inurl", []))
    engine.exclude(excludes or dorks_data.get("exclude", []))

    print(f"[DORK][BING] {engine}")
    engine.search()
