from pymongo import MongoClient
import certifi
from . import get_api_key

def connect(database: str, collection: str):
    mongodb_client = MongoClient(get_api_key.api_key(), tlsCAFile=certifi.where())
    database = mongodb_client.get_database(database)
    todo_list_collections = database[collection]
    return todo_list_collections
