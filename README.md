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

### Install playtest2

Install playtest2 in the virtual environment of your E2E test project:

```console
(.venv) $ python -m pip install playtest2
```

## Usage

### Gauge Configuration

1) Run `playtest2 setup` to automatically create `python.properties` in `env/default/`.

```console
(.venv) $ playtest2 setup

# If you have own step implementation directories
(.venv) $ playtest2 setup your_step_impl1 your_step_impl2
```

> [!TIP]
> Generated env/default/python.properties example
> ```
> STEP_IMPL_DIR = /**absolute**/path/of/your-project/.venv/lib/python3.x/site-packages/playtest2,your_step_impl1,your_step_impl2
> ```

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
