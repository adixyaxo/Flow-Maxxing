from dotenv import load_dotenv
import os
load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
JWT_KEY = os.getenv("JWT_KEY")
JWT_ALGO = os.getenv("JWT_ALGO")
JWT_EXP_TIME = int(os.getenv("JWT_EXP_TIME"))