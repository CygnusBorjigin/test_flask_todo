import json
from bson import json_util
from ast import literal_eval

from ..database_connection import *
import bcrypt

class UserManagement:
    def __init__(self):
        self.connection = database_connect.connect("todo_list", "user_info")


    def add_user(self, raw_data):
        user_dict = literal_eval(raw_data.decode('utf-8'))
        salt = bcrypt.gensalt()
        user_dict['userPassword'] = bcrypt.hashpw(bytes(user_dict['userPassword'], 'utf-8'), salt)
        self.connection.insert_one(user_dict)
        # do error management

    def list_user(self):
        collection_list = self.connection.find({})
        user_list = []
        for i in collection_list:
            user_list.append(i)
        return json.loads(json_util.dumps(user_list))