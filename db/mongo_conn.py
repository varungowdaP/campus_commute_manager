from pymongo import MongoClient

client = MongoClient("mongodb://localhost:27017/")
db = client["rides_database"]  # ✅ Your DB name
rides_col = db["rides"]        # ✅ Your Collection name
