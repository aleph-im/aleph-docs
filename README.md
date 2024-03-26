# Getting started

Based on _Material for MkDocs_

https://squidfunk.github.io/mkdocs-material/getting-started/

## Install Hatch

[Hatch](https://hatch.pypa.io/latest/) is a tool for managing Python projects.

```shell
pip install hatch
```

## Run the development server

Run the following command to get a server that will automatically update the docs pages whenever you edit the sources.

```shell
hatch run mkdocs serve
```

## Build the static site

Run the following command to build the static site. The result will be in the `site` directory.

```shell
hatch run mkdocs build
```

## Run test suites

This project uses [mktestdocs](https://github.com/koaning/mktestdocs) to check the validity of python code samples.
Code prefixed with `python` will be tested while code prefixed with `py` is not supposed to be a valid code (example: function signatures).

```shell
hatch run testing:test
```

