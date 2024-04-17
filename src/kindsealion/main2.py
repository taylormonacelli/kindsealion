import argparse
import pathlib

import jinja2


def get_template(template_name):
    TEMPLATES_PATH = pathlib.Path(__file__).resolve().parent / "templates"
    loader = jinja2.FileSystemLoader(searchpath=TEMPLATES_PATH)
    env = jinja2.Environment(loader=loader)
    return env.get_template(template_name)


def render_template(template_name, data=None):
    template = get_template(template_name)
    return template.render(data=data)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--outdir",
        type=pathlib.Path,
        help="Output directory",
        default="kindsealion",
    )
    return parser.parse_args()
