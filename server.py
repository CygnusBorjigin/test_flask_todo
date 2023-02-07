import json
from bson import json_util
from test_flask_todo.pkg.database_connection import *
from ast import literal_eval
from flask import Flask, request
import bcrypt
from .pkg.user_management.main import UserManagement


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
    u_m = UserManagement()

    u_m.add_user(raw_data)

    # hash the password

    return "this is signup"


@app.route("/listusers")
def list_users():
    todo_list_collections = database_connect.connect("todo_list", "user_info")
    collection_list = todo_list_collections.find({})
    user_list = []
    for i in collection_list:
        user_list.append(i)

    return json.loads(json_util.dumps(user_list))
