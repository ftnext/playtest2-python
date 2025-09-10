import argparse
import sys
from pathlib import Path


def setup(_):
    python_properties_dir = Path.cwd() / "env" / "default"
    python_properties_dir.mkdir(parents=True, exist_ok=True)
    playtest2_steps_dir = (
        Path(sys.prefix)
        / "lib"
        / f"python{sys.version_info.major}.{sys.version_info.minor}"
        / "site-packages"
        / "playtest2"
    )
    (python_properties_dir / "python.properties").write_text(
        f"""GAUGE_PYTHON_COMMAND = python
STEP_IMPL_DIR = {playtest2_steps_dir}"""
    )


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    setup_parser = subparsers.add_parser("setup", help="Set up gauge environment")
    setup_parser.set_defaults(func=setup)

    args = parser.parse_args()
    args.func(args)
