"""
Base class for spice simulator
"""
from pydantic import BaseModel, FilePath, DirectoryPath
from enum import Enum
from typing import List, Optional, Callable
import asyncio
from pywes.parse.results import ResultDict
import h5py
from asyncio import StreamReader


class SimulatorType(str, Enum):
    spice = "spice"
    em = "em"


class SimulationType(str, Enum):
    ac = "ac"
    dc = "dc"
    tran = "tran"


class BaseWrapper(BaseModel):
    name: str
    path: FilePath
    supported_sim: List[SimulationType]
    results: Optional[ResultDict]

    """
    Install the software on the machine.
    """
    install: Callable[[], bool]

    """
    Prepare the files needed for the simulation
    """
    prepare: Callable[[], bool]

    """
    Parse the output of the simulation and convert it to a ResultDict
    """
    parse_out: Callable[[StreamReader], ResultDict]
    parse_err: Callable[[StreamReader], ResultDict]

    """
    run the spice simulation describe by the _spice_file
    :param sim_file: input file to be simulated
    :param log_folder: directory to write simulation log
    :param config_file: List of file used to set up the simulator
    :return: a temp file of the raw out of the simulator (to be process by serialize_result)
    """

    async def run(
        self,
        sim_file: FilePath,
        log_folder: DirectoryPath,
        config_file: List[FilePath] = (),
    ):
        cir = open(sim_file)
        proc = await asyncio.create_subprocess_shell(
            f"{self.path} -s",
            stdin=cir,
            stdout=asyncio.subprocess.PIPE,
            stderr=asyncio.subprocess.PIPE,
        )
        std_out_task = asyncio.create_task(self.parse_out(proc.stdout))
        std_err_task = asyncio.create_task(self.parse_err(proc.stderr, log_folder))
        res = await asyncio.gather(proc.wait(), std_out_task, std_err_task)
        cir.close()
        print(res[1])
        self.results = res[1]

    def export(self, file: FilePath):
        with h5py.File(file, "w") as f:
            for res in self.results:
                f[f"res/{res}"] = self.results[res]
