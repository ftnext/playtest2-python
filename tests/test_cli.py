import sys

from playtest2.cli import main


def test_setup(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    sys.argv = ["playtest2", "setup"]
    main()

    python_properties_path = tmp_path / "env" / "default" / "python.properties"
    assert python_properties_path.exists()
    python_properties = python_properties_path.read_text().splitlines()
    assert python_properties[0] == "GAUGE_PYTHON_COMMAND = python"
    assert python_properties[1].startswith("STEP_IMPL_DIR =")
    assert python_properties[1].endswith("/site-packages/playtest2")


def test_setup_with_step_impl_dir(tmp_path, monkeypatch):
    monkeypatch.chdir(tmp_path)

    sys.argv = ["playtest2", "setup", "step_impl"]
    main()

    python_properties_path = tmp_path / "env" / "default" / "python.properties"
    assert python_properties_path.exists()
    python_properties = python_properties_path.read_text().splitlines()
    assert python_properties[0] == "GAUGE_PYTHON_COMMAND = python"
    assert python_properties[1].startswith("STEP_IMPL_DIR =")
    assert python_properties[1].endswith("/site-packages/playtest2,step_impl")
