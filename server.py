<<<<<<< HEAD
import jwt
from test_flask_todo.pkg.database_connection import *
=======
import json
from bson import json_util
>>>>>>> d6f0c980c91fc7105f364114319c0b296005e980
from ast import literal_eval
from flask import Flask, request
import bcrypt

from pkg.database_connection import database_connect
from .pkg.user_management.main import UserManagement
import datetime
import json
from bson import json_util
from .pkg.get_enviroment_variable.get_env_variable import get_var


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


@app.route("/signin")
def sign_in():
    raw_data = request.data
    user_dict = literal_eval(raw_data.decode('utf-8'))
    username = user_dict["userName"]
    user_entered_password = user_dict["userPassword"]
    todo_list_collections = database_connect.connect("todo_list", "user_info")
    usernames = todo_list_collections.find_one({"userName": username})
    clean_user = json.loads(json_util.dumps(usernames))
    if not usernames:
        # error handling and return
        pass
    entered_pass = user_entered_password.encode("utf-8")
    password = usernames["userPassword"]
    result = bcrypt.checkpw(entered_pass, password)
    if result:
        token_dict = {"_id": clean_user["_id"], "exp": datetime.datetime.utcnow() + datetime.timedelta(minutes=30)}
        secret = get_var("secret")
        token = jwt.encode(token_dict, secret)
        return {"jwt": token}
    else:
        return "not logged in"


