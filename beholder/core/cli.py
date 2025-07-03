import asyncclick as click
from beholder.engines.google import search_google_dorks
from beholder.engines.bing import search_bing_dorks


def parse_list(value):
    return [v.strip() for v in value.split(",")] if value else []


@click.command()
@click.argument("query", required=True)
@click.option(
    "-e",
    "--engine",
    type=click.Choice(["google", "bing"]),
    required=True,
    help="Search engine to use",
)
@click.option("-q", "--quoted-terms", help="List of quoted terms")
@click.option("-x", "--intext", help="List of terms in text/body")
@click.option("-t", "--intitle", help="List of page titles")
@click.option("-u", "--inurl", help="List of terms in urls")
@click.option("-s", "--site", help="List of sites")
@click.option("-d", "--domain", help="List of domains (bing only)")
@click.option("-E", "--exclude", help="List of excluded terms")
@click.option("-f", "--filetype", help="List of file extensions")
@click.option("-T", "--template", help="Dorks template name")
@click.option("-C", "--custom-template", help="Custom dorks template file")
async def search(
    query,
    engine,
    quoted_terms,
    intext,
    intitle,
    inurl,
    site,
    domain,
    exclude,
    filetype,
    template,
    custom_template,
):
    quoted_terms = parse_list(quoted_terms)
    texts = parse_list(intext)
    titles = parse_list(intitle)
    urls = parse_list(inurl)
    sites = parse_list(site)
    domains = parse_list(domain)
    excludes = parse_list(exclude)
    files = parse_list(filetype)

    if engine == "google":
        search_google_dorks(
            query,
            quoted_terms=quoted_terms,
            texts=texts,
            titles=titles,
            urls=urls,
            sites=sites,
            excludes=excludes,
            files=files,
            template=template,
            template_file=custom_template,
        )
    elif engine == "bing":
        search_bing_dorks(
            query,
            quoted_terms=quoted_terms,
            texts=texts,
            titles=titles,
            urls=urls,
            sites=sites,
            domains=domains,
            excludes=excludes,
            files=files,
            template=template,
            template_file=custom_template,
        )
    else:
        raise click.ClickException(f"Unsupported engine: {engine}")


@click.group()
async def cli():
    pass


cli.add_command(search)
