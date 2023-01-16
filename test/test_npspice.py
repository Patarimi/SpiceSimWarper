from pywes.wrapper.ngspice import NGSpice
from os import getcwd
from asyncio import run


def test_ngspice():
    run(NGSpice.run(f"{getcwd()}/test/schem_test.net", f"{getcwd()}/test/"))

    assert len(NGSpice.results.keys()) == 6

    NGSpice.export("./test/schem_test.hdf5")
