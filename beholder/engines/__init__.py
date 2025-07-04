import webbrowser


class BaseDorksEngine:
    def __init__(self):
        self.dork = ""
        self.search_url = ""

    def search(self):
        try:
            self._build_url()
            webbrowser.open_new(self.search_url)
            self.clear()
        except Exception as e:
            print(f"Error when starting broser: {e}")

    def clear(self):
        self.dork = ""
        self.search_url = ""

    def _make_query_by_args(self, rule: str, args: list[str]):
        if len(args) == 0:
            return

        query = [f"{rule}:{i}" for i in args]
        query = " | ".join(query)
        self.dork += f" {query}"

    def __str__(self):
        return self.dork.strip()
