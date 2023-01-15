"""The definition of the MetaData object



"""


class MetaData:
    """Provides easy interaction to the metadata json

    meta:
        Return: dictionary containing the raw metadata

    """

    def __init__(self, meta: dict) -> None:
        self.meta = meta

    def get_dates(self) -> list:
        """Returns all of the dates from the metadata as a MetaTag with a type of 'date'

        Returns:
            list: Contains MetaTag items with a type of 'date'
        """

        tags = []

        return tags

    def get_files(self) -> list:
        """Returns all of the file paths from the metadata as a MetaTag with a type of 'path'

        Returns:
            list: Contains MetaTag items with a type of 'path'
        """

        tags = []

        return tags
