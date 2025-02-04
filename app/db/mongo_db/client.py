import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

MONGO_URL = os.getenv("MONGO_URL")
DB_YAD2 = os.getenv("DB_YAD2")

client = MongoClient(MONGO_URL)

# Access a specific database and collection (optional example)
db_yad2 = client[DB_YAD2]  # Replace with your database name



