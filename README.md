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

### Setting up Gauge with playtest2

1. Create a new dedicated virtual environment for Gauge in a **separate** directory from your E2E test project:

```console
$ mkdir /path/to/gauge-project  # Specify your own path here
$ cd /path/to/gauge-project
$ python -m venv .venv --upgrade-deps
$ source .venv/bin/activate
```

2. Install playtest2 in the virtual environment:

```console
(.venv) $ python -m pip install playtest2
```

## Usage

### Gauge Configuration

Edit `python.properties` in `env/default/`.

```
STEP_IMPL_DIR = /**absolute**/path/of/gauge-project/.venv/lib/python3.x/site-packages/playtest2
```

Create `playtest2.properties` in `env/default/`.

```
SUT_BASE_URL = http://127.0.0.1:8000
```

On activating the virtual environment for Gauge, run `gauge` command in your E2E test project:

```console
(.venv) $ cd /path/to/e2e/project
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
