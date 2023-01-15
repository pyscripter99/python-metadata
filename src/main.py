"""Contains the fundamental code for editing metadata

"""

import os
import inspect
import json
import magic
from internals.metadata import MetaData

class_registry = {}

# Discover all files in the 'handlers' directory
for file_name in os.listdir(
    os.path.join(os.path.dirname(os.path.realpath(__file__)), "handlers")
):
    # check if the file is a python file
    if file_name.endswith(".py") and not file_name.startswith("_"):
        # import the module
        module_name = file_name[:-3]
        imported_module = __import__(f"handlers.{module_name}", fromlist=["handlers"])
        # check if the imported module contains the class 'Handler'
        for name, obj in inspect.getmembers(imported_module):
            if inspect.isclass(obj) and obj.__name__ == "Handle":
                class_registry[json.dumps(obj().handles)] = obj


def read(file_path: str) -> MetaData:
    """Returns a MetaData object containing the metadata from the file

    Args:
        file_path (str): The full path to any file

    Returns:
        MetaData: Contains helpful interactions with the json, in a seamless way
    """
    mime = magic.Magic(mime=True)
    mime = mime.from_file(file_path)
    print(mime)
