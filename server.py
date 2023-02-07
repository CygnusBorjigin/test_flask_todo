import json
from bson import json_util
from ast import literal_eval
from flask import Flask, request
import bcrypt

from pkg.database_connection import database_connect
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


    return "this is signup"


@app.route("/listusers")
def list_users():
    u_m = UserManagement()
    return u_m.list_user()



