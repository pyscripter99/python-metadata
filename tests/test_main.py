"""Test the main function
"""

from src import main as py_meta
from src.internals.metadata import MetaData


def test_read():
    """Tests for a MetaData object returned."""
    assert isinstance(py_meta.read("demo_file.jpg"), MetaData)
