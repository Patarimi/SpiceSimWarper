import shutil

from pywas.main import new_project


def test_new_project():
    rdm_dir_name = "bawaah"
    new_project(name=rdm_dir_name)
    f = open(rdm_dir_name + "/config.yaml")
    f.close()
    shutil.rmtree(rdm_dir_name)
