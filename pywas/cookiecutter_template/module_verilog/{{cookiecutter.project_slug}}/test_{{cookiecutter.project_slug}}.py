import cocotb
{% if cookiecutter.testing_software == "cocotb-test" %} import os
from cocotb_test.simulator import run {% endif %}


@cocotb.test()
async def runtine_{{cookiecutter.project_slug}}(dut):
    assert False

{% if cookiecutter.testing_software == "cocotb-test" %}
def test_{{cookiecutter.project_slug}}():
	run(
		verilog_sources=["{{cookiecutter.project_slug}}/{{cookiecutter.project_slug}}.v"],
		toplevel="{{cookiecutter.project_slug}}",
		module="test_{{cookiecutter.project_slug}}",
		timescale="1ns/1ps",
		work_dir=os.path.join(os.curdir, "{{cookiecutter.project_slug}}"),
	)
{% endif %}
