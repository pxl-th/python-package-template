# Python Package Template

Contains minimal python package structure.

# Table of contents

# How to install

To install package, execute

```bash
python setup.py install .
```

or install a project in editable mode

```bash
python setup.py install -e .[dev]
```

# Run tests

To run tests, execute

```bash
python setup.py test
```

# Build documentation

If you are building documentation for the first time,
or you have changed package structure, execute

```bash
sphinx-apidoc -o docs/ template
```

**Note** if there are no changes, then you should delete files,
that already exist in the list produced by command above.
And then execute

```bash
python setup.py build_sphinx
```
