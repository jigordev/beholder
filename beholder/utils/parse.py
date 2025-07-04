import json
from collections import defaultdict


def load_json_vars(json_file: str) -> dict:
    with open(json_file, "r") as f:
        return json.load(f)


def parse_key_value_args(var_args: list[str]) -> dict:
    context = defaultdict(list)
    for arg in var_args:
        key, value = arg.split("=", 1)
        values = value.split(",")
        context[key].extend(values if len(values) > 1 else values)
    return dict(context)
