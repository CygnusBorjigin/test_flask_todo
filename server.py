from flask import Flask
from pymongo import MongoClient
from flask import request
import json
import certifi
import datetime
from ast import literal_eval


app = Flask(__name__)

@app.route("/")
def still_working():
    return "still working"

@app.route("/document_count")
def count_document():
    config_file = open("./config.json", "r")
    content = json.load(config_file)
    apiKey = content["mongoDBConnection"]
    config_file.close()
    mongodb_client = MongoClient(apiKey, tlsCAFile=certifi.where())
    database = mongodb_client.get_database("todo_list")
    todo_list_collections = database.test_todo
    return str(todo_list_collections.count_documents({})) + "\n"

@app.route("/signup")
def user_signup():
    raw_data = request.data
    my_dict = literal_eval(raw_data.decode('utf-8'))
    print(my_dict['userName'])
    return "this is signup"