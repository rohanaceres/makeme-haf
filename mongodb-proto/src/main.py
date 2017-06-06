# -*- coding: utf-8 -*-

from app.services.mongo_service import MongoService
from datetime import datetime

def main():
    mongoService = MongoService("CasasBahia")
    mongoService.insert({"author": "Vivi", "text": "My first blog post!", "tags": ["mongodb", "python", "pymongo"], "date": datetime.utcnow()})
    r = mongoService.get({"author": "Vivi"})
    print (r['text'])
    mongoService.delete()

if __name__ == "__main__":
    main()