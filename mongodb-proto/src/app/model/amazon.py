from bson.objectid import ObjectId

""" Mocked model. """
class Amazon(object):
    def __init__ (self, id=None, carrot1=None, carrot2=None, carrotNumber=123):
        if id is None:
            self._id = ObjectId()
        else:
            self._id = id
        self.carrot1 = carrot1
        self.carrot2 = carrot2
        self.carrotNumber = carrotNumber
    
    def get_as_json (self):
        return self.__dict__