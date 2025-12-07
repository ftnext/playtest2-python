import argparse
import sys
from pathlib import Path


def setup(args):
    python_properties_dir = Path.cwd() / "env" / "default"
    python_properties_dir.mkdir(parents=True, exist_ok=True)

    step_impl_dirs: list[str] = []
    playtest2_steps_dir = (
        Path(sys.prefix)
        / "lib"
        / f"python{sys.version_info.major}.{sys.version_info.minor}"
        / "site-packages"
        / "playtest2"
    )
    step_impl_dirs.append(str(playtest2_steps_dir))

    step_impl_dirs.extend(str(path) for path in args.step_impl_dir)

    (python_properties_dir / "python.properties").write_text(
        f"""GAUGE_PYTHON_COMMAND = python
STEP_IMPL_DIR = {",".join(step_impl_dirs)}"""
    )


def main():
    parser = argparse.ArgumentParser()
    subparsers = parser.add_subparsers(dest="command", required=True)

    setup_parser = subparsers.add_parser("setup", help="Set up gauge environment")
    setup_parser.add_argument("step_impl_dir", type=Path, nargs="*", help="Step implementation directory")
    setup_parser.set_defaults(func=setup)

    args = parser.parse_args()
    args.func(args)
