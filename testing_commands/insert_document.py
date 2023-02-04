from pymongo import MongoClient
import json
import certifi

config_file = open("../config.json", "r")
content = json.load(config_file)
apiKey = content["mongoDBConnection"]
config_file.close()

mongodb_client = MongoClient(apiKey, tlsCAFile=certifi.where())
database = mongodb_client.get_database("todo_list")
todo_list_collections = database.test_todo
found_message = todo_list_collections.find_one({
    "user": "someone2"
})
print(found_message)