from pymongo.mongo_client import MongoClient
from src.config.environment import MONGO_URL


conn = MongoClient(MONGO_URL).flow_maxxing
notes_DB = conn.notes
users_DB = conn.users
tasks_DB = conn.tasks