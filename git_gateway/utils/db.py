from pymongo import MongoClient
from os import environ

mongo_client = MongoClient(f"mongodb://{environ.get('MONGO_HOST')}:{environ.get('MONGO_PORT')}")


