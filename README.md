# python-MetaData

## About

This is a library that helps you to easily extract and edit metadata of files. The library is easy to use, and it can be used to extract metadata from any kind of file, such as photos, videos, documents, audio files, and more.

The read function returns a MetaData object that contains the metadata of a file. It is able to determine the type of file and extract the metadata accordingly. With this function, you can access all the relevant metadata information of a file in an easy to use object format.

The write function allows you to edit the metadata of a file. You can use this function to add or modify metadata of a file to help you better organize and index your files. This can be useful for many use cases such as adding tags, titles, descriptions, etc.

This library is designed to be simple to use and it doesn't require you to have any technical knowledge about how it works. With this library, you can easily manage and organize your files with rich metadata information.

## Usage

``` python
import python_metadata as py_meta

# read metadata
metadata = py_meta.read("path/to/file")

# print
print(metadata)

# result:
# Camera: Pixel 6 Pro
# ...

# edit
metadata.camera = "Pixel 6" # <MetaData>.camera contains the camera feild with automatic formatting,  for manual editing, use metadata.raw["camera"] to manually edit. use metadata.json to export metadata to json (this creates a NEW object, changes will not apply)

# write
py_meta.write("path/to/file", metadata)
```