"""Test the main function
"""

import requests
from src import main as py_meta
from src.internals.metadata import MetaData

image = requests.get(
    "https://file-examples.com/storage/fea8fc38fd63bc5c39cf20b/2017/10/file_example_JPG_500kB.jpg",
    timeout=6,
)
with open("demo_file.jpg", "wb") as f:
    f.write(image.content)


def test_read():
    """Tests for a MetaData object returned."""
    assert isinstance(py_meta.read("demo_file.jpg"), MetaData)
