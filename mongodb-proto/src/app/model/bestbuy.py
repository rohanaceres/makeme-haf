"""
ObjectId: responsible for generate new IDs (PK) for an object.
"""
from bson.objectid import ObjectId

class BestBuy(object):
    """
    BestBuy mocked model.
    """
    def __init__(self, _id=None, potato1=None, potato2=None, potato_number=123):
        if _id is None:
            self._id = ObjectId()
        else:
            self._id = _id
        self.potato1 = potato1
        self.potato2 = potato2
        self.potato_number = potato_number

    def get_as_json(self):
        """
        Get the oblect as JSON.
        """
        return self.__dict__

    