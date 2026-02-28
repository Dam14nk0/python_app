from flask_jwt_extended import JWTManager
from pymongo import MongoClient

jwt = JWTManager()
mongo_client: MongoClient | None = None


def init_mongo(uri: str) -> MongoClient:
    global mongo_client
    mongo_client = MongoClient(uri)
    return mongo_client
