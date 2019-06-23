from setuptools import (
    find_packages,
    setup,
)

VERSION = "0.0.1"


setup(
    name="template",
    version=VERSION,
    command_options={
        "build_sphinx": {
            "version": ("setup.py", VERSION),
            "release": ("setup.py", VERSION),
        },
    },
    license="MIT",
    description="Template package structure.",
    classifiers=[
        "License :: MIT",
        "Programming Language :: Python :: 3 :: Only",
    ],
    packages=find_packages(include=["template"]),
    python_requires=">=3.7",
    setup_requires=[
        "pip>=19.1",
        "setuptools>=41",
        "pytest-runner>=5.1",
    ],
    install_requires=[],
    extras_require={
        "dev": [
            "sphinx>=2.1",
        ],
    },
    tests_require=[
        "coverage>=4.5",
        "flake8-quotes>=2.0",
        "pytest-cov>=2.7",
        "pytest-flake8>=1.0",
        "pytest-pylint>=0.14",
    ],
)
