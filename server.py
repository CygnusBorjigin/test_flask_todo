from flask import Flask
from pymongo import MongoClient
from flask import request
import json
import certifi
from ast import literal_eval
from helper_functions import *


app = Flask(__name__)

@app.route("/")
def still_working():
    database_connect.connect("todo_list", "test_todo")
    return "still working"

@app.route("/document_count")
def count_document():
    todo_list_collections = database_connect.connect("todo_list", "test_todo")
    return str(todo_list_collections.count_documents({})) + "\n"

@app.route("/signup")
def user_signup():
    raw_data = request.data
    my_dict = literal_eval(raw_data.decode('utf-8'))
    todo_list_collections = database_connect.connect("todo_list", "user_info")
    todo_list_collections.insert_one(my_dict)
    return "this is signup"

@app.route("/listusers")
def list_users():
    todo_list_collections = database_connect.connect("todo_list", "user_info")
    collection_list = todo_list_collections.find({})
    for x in collection_list:
        print(x)
    return str(collection_list)
