# Python Packaging Guidelines

## Project Structure
```
project/
├── src/
│   └── mypackage/
│       ├── __init__.py
│       └── module.py
├── tests/
├── pyproject.toml
├── README.md
└── requirements.txt
```

## Dependency Management
- Use virtual environments for isolation
- Pin dependency versions in requirements.txt
- Use requirements-dev.txt for development dependencies

## Setup Configuration
```toml
[build-system]
requires = ["setuptools>=45", "wheel"]
build-backend = "setuptools.build_meta"

[project]
name = "mypackage"
version = "0.1.0"
description = "A sample package"
dependencies = [
    "requests>=2.25.0",
    "click>=7.0",
]
```

## Distribution
- Use semantic versioning (MAJOR.MINOR.PATCH)
- Include comprehensive README and CHANGELOG
- Use GitHub Actions for CI/CD
- Publish to PyPI using twine
