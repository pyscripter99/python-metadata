"""Template for metadata processor

read file_path:
    file_path -- The full path to the file to be processed
    Return: A MetaData object
    
write file_path meta:
    file_path -- The full path to the file to be processed
    meta      -- the MetaData object containing the changes
    Return: None
"""

# name accordingly e.g. pngHandler.py
from ..internals.metadata import MetaData


class Handle:
    def __init__(self) -> None:
        self.handles = [
            "image/png"
        ]  # can use mimetypes ( image/*, text/plain ) or file extensions ( png, jpg, txt )

    def read(self, file_path: str):
        # do some metadata processing

        mime = (
            {}
        )  # {"dateCreated": "2018-08-18  11:19:42 AM", "camera": "Google Pixel 6 Pro"}

        return MetaData(mime)

    def write(self, file_path: str, meta: MetaData):
        # write some metadata
        pass
