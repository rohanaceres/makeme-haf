"""
ObjectId: responsible for generate new IDs (PK) for an object.
"""
from bson.objectid import ObjectId

class Amazon(object):
    """
    Amazon mocked model.
    """
    def __init__(self, _id=None, carrot1=None, carrot2=None, carrot_number=123):
        if _id is None:
            self._id = ObjectId()
        else:
            self._id = _id
        self.carrot1 = carrot1
        self.carrot2 = carrot2
        self.carrot_number = carrot_number

    def get_as_json(self):
        """
        Get the oblect as JSON.
        """
        return self.__dict__
