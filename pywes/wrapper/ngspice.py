from asyncio import StreamReader
from pydantic import FilePath, DirectoryPath
from .base_wrapper import BaseWrapper, ResultDict
from typer import Typer
import wget
import zipfile
from os import getcwd, remove

ng_spice = Typer()


async def parse_out(stdout: StreamReader) -> ResultDict:
    ind = 0
    var_name = list()
    step = "start"
    results = ResultDict()
    while line := await stdout.readline():
        l_str = line.decode()
        if l_str.startswith("Variables"):
            step = "var_name"
        if l_str.startswith("Values"):
            step = "values"
            continue
        l_split = l_str.split()
        # Variables name part
        if step == "var_name" and len(l_split) == 3:
            try:
                int(l_split[0])
            except ValueError:
                continue
            var_name.append(l_split[1])
            results[l_split[1]] = list()
            continue
        # Values extractions part
        if step == "values":
            if len(l_split) == 2:
                ind = 0
                results[var_name[ind]].append(float(l_str.split()[1]))
            else:
                r = float(l_str)
                ind += 1
                results[var_name[ind]].append(r)
    return results


async def parse_err(stderr: StreamReader, log_folder: DirectoryPath):
    with open(log_folder + "err.out", "wb") as err:
        err.write(await stderr.read())


@ng_spice.command()
def install():
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


@ng_spice.command()
def prepare() -> bool:
    return True


NGSpice = BaseWrapper(
    name="ngspice",
    path=f"{getcwd()}/simulators/Spice64/bin/ngspice_con.exe",
    supported_sim=("ac",),
    parse_out=parse_out,
    parse_err=parse_err,
    install=install,
    prepare=prepare,
)
