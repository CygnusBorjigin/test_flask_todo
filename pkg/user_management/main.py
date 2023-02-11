from bson import json_util
from ast import literal_eval
from ..database_connection import *
from ..get_enviroment_variable.get_env_variable import get_var

import bcrypt
import json
import jwt
import datetime


class UserManagement:
    def __init__(self):
        self.__connection = database_connect.connect("todo_list", "user_info")

    def add_user(self, raw_data):
        """
        Adds a user to the database after parsing through a json file
        :param raw_data: Json data that contains a username and password
        :return: None
        """
        user_dict = literal_eval(raw_data.decode('utf-8'))
        salt = bcrypt.gensalt()
        user_dict['userPassword'] = bcrypt.hashpw(bytes(user_dict['userPassword'], 'utf-8'), salt)
        self.__connection.insert_one(user_dict)
        # do error management

    def list_user(self):
        """
        Returns a json file of all the users and their information
        :return: json file after converting from Cursor object to a list to json format
        """
        collection_list = self.__connection.find({})
        user_list = []
        for i in collection_list:
            user_list.append(i)
        return json.loads(json_util.dumps(user_list))

    def sign_in_user(self, raw_data):
        """
        Validates username and password
        If valid, returns a token
        Else, returns Error
        :return:
        """
        user_dict = literal_eval(raw_data.decode('utf-8'))

        username = user_dict["userName"]
        user_entered_password = user_dict["userPassword"]

        usernames = self.__connection.find_one({"userName": username})
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

