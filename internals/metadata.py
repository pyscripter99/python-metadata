"""The definition of the MetaData object



"""


class MetaData:
    """Provides easy interaction to the metadata json

    meta:
        Return: dictionary containing the raw metadata

    """

    def __init__(self, meta: dict) -> None:
        self.meta = meta
        # TODO: add processing
