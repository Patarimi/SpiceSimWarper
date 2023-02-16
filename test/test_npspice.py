from pywas.wrapper.ngspice import NGSpice
from asyncio import run


def test_ngspice():
    run(NGSpice.run(f"./test/schem_test.net", f"./test/"))

    assert len(NGSpice.results.keys()) == 6

    NGSpice.export("./test/schem_test.hdf5")
