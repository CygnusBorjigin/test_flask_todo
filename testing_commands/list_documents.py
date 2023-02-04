from pymongo import MongoClient
import certifi
import json


config_file = open("../config.json", "r")
content = json.load(config_file)
apiKey = content["mongoDBConnection"]
config_file.close()

mongodb_client = MongoClient(apiKey, tlsCAFile=certifi.where())
database = mongodb_client.get_database("todo_list")
todo_list_collections = database.test_todo
print(todo_list_collections.count_documents({}))