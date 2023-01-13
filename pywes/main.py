import typer
import wget
import zipfile
from os import getcwd, remove
from .wrapper.ngspice import ng_spice

cli = typer.Typer()
cli.add_typer(ng_spice, "ngspice")


@cli.command()
def install_ngspice():
    """
    Install ngspice executable in the correct location.
    """
    ngspice_version = 38
    ngspice_base_url = f"https://sourceforge.net/projects/ngspice/files/ng-spice-rework/{ngspice_version}/"
    ngspice_archive_name = f"ngspice-{ngspice_version}_64.zip"
    base_install = f"{getcwd()}/simulators/"
    wget.download(ngspice_base_url + ngspice_archive_name, base_install)
    with zipfile.ZipFile(base_install + ngspice_archive_name) as zip:
        zip.extractall(base_install)
    remove(base_install + ngspice_archive_name)


if __name__ == "__main__":
    cli()
