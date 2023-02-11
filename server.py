import jwt
import datetime
import json
import bcrypt

from ast import literal_eval
from flask import Flask, request
from bson import json_util

from .pkg.database_connection.database_connect import connect
from .pkg.user_management.main import UserManagement
from .pkg.get_enviroment_variable.get_env_variable import get_var


app = Flask(__name__)


@app.route("/")
def still_working():
    connect("todo_list", "test_todo")
    return "still working"


@app.route("/document_count")
def count_document():
    todo_list_collections = connect("todo_list", "test_todo")
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


@app.route("/signin")
def sign_in():
    raw_data = request.data
    u_m = UserManagement()
    return u_m.sign_in_user(raw_data)


