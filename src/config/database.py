from pymongo.mongo_client import MongoClient
from src.config.environment import MONGO_URL

conn = MongoClient(MONGO_URL).notes
