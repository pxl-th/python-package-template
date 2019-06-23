"""
Simple test for package.
"""
from template import __version__


def test_version():
    """
    Check that `__version__` exists.
    """
    assert isinstance(__version__, str)
