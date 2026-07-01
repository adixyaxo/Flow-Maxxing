from pymongo.mongo_client import MongoClient
from src.config.environment import MONGO_URL
from motor.motor_asyncio import AsyncIOMotorClient

Client = AsyncIOMotorClient(MONGO_URL)
conn = Client.flow_maxxing
notes_DB = conn.notes
users_DB = conn.users
tasks_DB = conn.tasks