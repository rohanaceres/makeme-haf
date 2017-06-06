from bson.objectid import ObjectId

""" Mocked model. """
class BestBuy(object):
    def __init__ (self, id=None, potato1=None, potato2=None, potatoNumber=123):
        if id is None:
            self._id = ObjectId()
        else:
            self._id = id
        self.potato1 = potato1
        self.potato2 = potato2
        self.potatoNumber = potatoNumber
    
    def get_as_json (self):
        return self.__dict__
        
    