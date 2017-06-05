# -*- coding: utf-8 -*-

from app.services.mongo_service import MongoService

def main():
    mongoService = MongoService()
    mongoService.create()
    mongoService.delete()

if __name__ == "__main__":
    main()