import os
from rich import print
import typer
from .wrapper.ngspice import ng_spice
from .wrapper.base_wrapper import write_conf
from .wrapper.template import template

"""could be :
    from importlib import import_module
    module = import_module(var: str)
"""
help = """
*Py*thon *W*rapper for *A*nalog design *S*oftware

**Installation using [pipx](https://pypa.github.io/pipx/installation/)**:

```console
$ pipx install pywas
```
"""
cli = typer.Typer(help=help)
cli.add_typer(ng_spice, name="ngspice")
cli.add_typer(template, name="template")


@cli.command("create")
def new_project(name: str, flow: str = typer.Argument("OpenLane")):
    """
    Create a new project with specified options.
    """
    os.mkdir(name)
    write_conf({"flow": flow}, os.path.join(name, "config.yaml"))
    print("new project created !")


if __name__ == "__main__":
    cli()
