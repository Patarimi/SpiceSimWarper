import os

from cookiecutter.exceptions import RepositoryNotFound
from rich import print, pretty
import typer
from .wrapper.ngspice import ng_spice
from pywas.template import template
from cookiecutter.main import cookiecutter


help_str = """
*Py*thon *W*rapper for *A*nalog design *S*oftware

**Installation using [pipx](https://pypa.github.io/pipx/installation/)**:

```console
$ pipx install pywas
```
"""
cli = typer.Typer(help=help_str)
cli.add_typer(ng_spice, name="ngspice", help="ngspice utility")
cli.add_typer(template, name="template", help="templating part")


@cli.command("create")
def new_project(name: str):
    """
    Create a new project with specified options.
    """
    template_path = "./pywas/cookiecutter_template"
    try:
        cookiecutter(os.path.join(template_path, name))
    except RepositoryNotFound:
        print(f"{name} not found. Available template are :")
        for k in os.listdir(template_path):
            print(f"\t- {k}")


if __name__ == "__main__":
    cli()
