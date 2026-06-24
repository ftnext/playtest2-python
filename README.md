# playtest2

[![PyPI - Version](https://img.shields.io/pypi/v/playtest2.svg)](https://pypi.org/project/playtest2)
[![PyPI - Python Version](https://img.shields.io/pypi/pyversions/playtest2.svg)](https://pypi.org/project/playtest2)

-----

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Development](#development)
- [License](#license)

## Installation

### Prerequisites

* [Gauge](https://docs.gauge.org/getting_started/installing-gauge)
* [uv](https://docs.astral.sh/uv/) (or [pipx](https://pipx.pypa.io/stable/)) for installing the `playtest2` setup command

### Setting up Gauge with playtest2

1. Install `playtest2` as a uv tool:

```console
$ uv tool install playtest2
```

This provides the `playtest2 setup` command from an isolated environment outside your E2E test project.

2. Create a virtual environment for your E2E test project:

```console
$ cd /path/to/e2e/project
$ python -m venv .venv --upgrade-deps
$ source .venv/bin/activate
```

3. Install `playtest2` in the E2E virtual environment too:

```console
(.venv) $ python -m pip install playtest2
```

The uv tool installation is used for generating Gauge configuration. The E2E virtual environment installation is used when Gauge runs the Python steps.

## Usage

### Gauge Configuration

1) From the E2E test project root, run the uv tool-installed `playtest2 setup` to create `python.properties` in `env/default/`.

```console
$ playtest2 setup

# If you have own step implementation directories
$ playtest2 setup your_step_impl1 your_step_impl2
```

> [!TIP]
> Generated env/default/python.properties example
> ```
> STEP_IMPL_DIR = /**absolute**/path/of/uv/tool/environment/lib/python3.x/site-packages/playtest2,your_step_impl1,your_step_impl2
> ```

> [!IMPORTANT]
> Run `playtest2 setup` using the uv tool-installed command, not the command inside your E2E project's `.venv`.
> This keeps `site-packages/playtest2` outside the E2E project directory and avoids Gauge Python loader issues with project-local `.venv` paths.

2) Create `playtest2.properties` in `env/default/`.

```
SUT_BASE_URL = http://127.0.0.1:8000
```

Run `gauge` command in your E2E test project:

```console
(.venv) $ gauge run specs
```

### Spec example

```markdown
# サンプルアプリのテスト

## GETリクエストが送れる

* パス"/"に
* メソッド"GET"で
* リクエストを送る

* レスポンスのボディが
* JSONのパス"$.message"に対応する値が
* 文字列の"Hello World"である
```

## Development

Prerequisites: **Hatch** ([Installation](https://hatch.pypa.io/latest/install/))

### Lint

```bash
hatch fmt && hatch run types:check
```

### Test

```bash
hatch test --randomize --doctest-modules
```

## License

`playtest2` is distributed under the terms of the [MIT](https://spdx.org/licenses/MIT.html) license.
