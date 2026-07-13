# greet-rune

Greet Rune using this Python package.

## Installation

The package is published to TestPyPI, so install it from that index:

```sh
uv add --index https://test.pypi.org/simple/ greet-rune
```

## Usage

```python
from greet_rune import greet_py, greet_rust

greet_py()    # Hi Rune!
greet_rust()  # Hi Rune!
```

## Development

Build Rust extension:

`maturin develop`

Run tests:

`uv run --extra tests pytest`


### Version


Note that we're using `dynamic = ["version"]` in `pyproject.toml`, which tells maturin to read the package version from the `[package]` `version` field in `Cargo.toml`.

