import json
from ..get_enviroment_variable.get_env_variable import get_var


def api_key():
    key = get_var("mongoDBConnection")
    return key