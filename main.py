import os
import inspect

class_registry = {}

# Discover all files in the 'handlers' directory
for file_name in os.listdir("handlers"):
    # check if the file is a python file
    if file_name.endswith(".py") and not file_name.startswith("_"):
        # import the module
        module_name = file_name[:-3]
        imported_module = __import__(f"handlers.{module_name}", fromlist=["handlers"])
        # check if the imported module contains the class 'Handler'
        for name, obj in inspect.getmembers(imported_module):
            if inspect.isclass(obj) and obj.__name__ == "Handler":
                class_registry[obj.handles] = obj


print(class_registry)
