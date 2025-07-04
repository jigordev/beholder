from jinja2 import Template, StrictUndefined
from pathlib import Path


def render_dorks_template(template_path: Path, context) -> str:
    if not template_path.exists():
        raise FileNotFoundError(f"Template not found: {template_path}")

    template_str = template_path.read_text()
    template = Template(
        template_str, undefined=StrictUndefined, trim_blocks=True, lstrip_blocks=True
    )
    return template.render(**context)
