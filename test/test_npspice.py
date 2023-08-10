from pywas.wrapper.ngspice import NGSpice
from asyncio import run


def test_ngspice(tmp_path):
    run(NGSpice.run("./test/schem_test.net", tmp_path / "test"))

    assert len(NGSpice.results.keys()) == 6

    NGSpice.export(tmp_path / "test/schem_test.hdf5")
