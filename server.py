from helper_functions import *
from ast import literal_eval
from flask import request
from flask import Flask
import bcrypt


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

    # hash the password
    salt = bcrypt.gensalt()
    my_dict['userPassword'] = bcrypt.hashpw(bytes(my_dict['userPassword'], 'utf-8'), salt)

    todo_list_collections.insert_one(my_dict)
    return "this is signup"

@app.route("/listusers")
def list_users():
    todo_list_collections = database_connect.connect("todo_list", "user_info")
    collection_list = todo_list_collections.find({})
    for x in collection_list:
        hashed = x["userPassword"]

        print(x)

    return str(collection_list)



