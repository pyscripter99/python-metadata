"""Template for metadata processor

"""
import os
from internals.metadata import MetaData

# name accordingly e.g. pngHandler.py


class Handle:

    """Provides functions for internal use
    read file_path:
        file_path -- The full path to the file to be processed
        Return: A MetaData object
    write file_path meta:
        file_path -- The full path to the file to be processed
        meta      -- the MetaData object containing the changes
        Return: None
    """

    def __init__(self) -> None:
        self.handles = [
            "image/png",
            "image/jpeg",
            "application/x-ppm",
            "image/gif",
            "image/tiff",
            "image/bmp",
        ]  # can use mimetypes ( image/*, text/plain ) or file extensions ( png, jpg, txt )

    def read(self, file_path: str):
        """Loads the metadata from any given path

        Args:
            file_path (str): The full path to the file

        Returns:
            MetaData: Contains all additional file information
        """
        # do some metadata processing
        os.path.getctime(file_path)

        mime = (
            {}
        )  # {"dateCreated": "2018-08-18  11:19:42 AM", "camera": "Google Pixel 6 Pro"}

        return MetaData(mime)

    def write(self, file_path: str, meta: MetaData):
        """Writes the metadata from MetaData object to the path

        Args:
            file_path (str): The full path to the file
            meta (MetaData): The object containing the metadata
        """
