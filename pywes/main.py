import typer
from .wrapper.ngspice import ng_spice

cli = typer.Typer()
cli.add_typer(ng_spice, name="ngspice")


if __name__ == "__main__":
    cli()
