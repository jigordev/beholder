import asyncclick as click
from beholder.engines import get_search_url
from beholder.core.templates import render_dorks_template
from beholder.core.browser import open_webbrowser
from beholder.utils.parse import load_json_vars, parse_key_value_args
from beholder.utils.paths import get_data_path


@click.command()
@click.option(
    "-e",
    "--engine",
    type=click.Choice(["google", "bing"]),
    required=True,
    help="Search engine to use",
)
@click.option(
    "-v", "--var", multiple=True, help="Specify dork template variables key=value"
)
@click.option("-j", "--json-file", help="Specify variables from json file")
@click.option("-t", "--template", help="Dorks template name")
@click.option("-T", "--template-file", help="Custom dorks template file")
async def search(engine, var, json_file, template, template_file):
    if not template and not template_file:
        raise click.UsageError("You must specify either --template or --template-file.")

    data = {}

    if json_file:
        data = load_json_vars(json_file)
    else:
        data = parse_key_value_args(var)

    template_path = None
    if template:
        template_path = get_data_path("templates", engine, template)
    else:
        template_path = template_file

    try:
        dork = render_dorks_template(template_path, data)
        click.echo(f"[DORK][{engine.upper()}]: {dork}")
    except Exception as e:
        raise click.ClickException(f"Failed to render dork template: {e}")

    search_url = get_search_url(engine, dork)

    try:
        open_webbrowser(search_url)
    except Exception as e:
        raise click.ClickException(f"Failed to open browser: {e}")


@click.group()
async def cli():
    pass


cli.add_command(search)
