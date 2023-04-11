from pywas.main import new_project


def test_new_project(tmp_path):
    rdm_dir_name = tmp_path / "bawaah"
    new_project(name=rdm_dir_name)
    f = open(rdm_dir_name / "config.yaml")
    f.close()
