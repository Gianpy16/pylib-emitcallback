# 📶 Python Library - emitcallback (Emit Callback)

Python library that implements callable collectors to call to react on an event.

Use cases are reducing the amount of coupling, components systems, events systems and games.
This project is inspired from Godot's game engine signals.

In this repository you'll find the source of the library and the source of his sphinx documentation build using [read the docs](https://about.readthedocs.com/).

Releases of this library have been published to PyPi package manager.

## Install

See here to install using pip:
- https://pypi.org/project/emitcallback/

## Documentation

See the docs about the contents and example.
- https://pylib-emitcallback.readthedocs.io/en/latest/

## Build - Weel package with Hatch

Dependencies: [Hatch](https://hatch.pypa.io/1.12/)

Run the following:

```
python -m hatch build
```

## Build - Sphinx documentation

Dependencies: [Sphinx](https://www.sphinx-doc.org/en/master/index.html), [Python's Doc Theme](https://pypi.org/project/python-docs-theme/)

Run the following:

```
sphinx-build -M html ./docs/ ./build --fail-on-warning -a
```
