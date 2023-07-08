from pymongo.mongo_client import MongoClient
from .configs import Configs
from lib.configs.constants import DBConstants

class MongoDBClient:
    def __init__(self):
        self.client = MongoClient(Configs.DB_CONNECTION_STRING)
        self.db = self.client[Configs.DB_NAME]
        self.collection = self.db[Configs.DB_COLLECTION_NAME]
        self.__connnect()
        self.existing_topics = [str(value) for value in self.collection.distinct(DBConstants.TOPIC)]

    def __connnect(self):
        try:
            self.db.command('ping')
        except Exception as e:
            raise e
