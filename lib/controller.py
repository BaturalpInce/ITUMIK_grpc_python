from lib.utils.mongo_client import MongoDBClient
from lib.validators import mongo_validators

class APIController:
    def __init__(self):
        self.mongo_client = MongoDBClient() if mongo_validators.check_mongodb_parameters() else None