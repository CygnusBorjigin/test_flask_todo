import json

def api_key():
    config_file = open("./config.json", "r")
    content = json.load(config_file)
    apiKey = content["mongoDBConnection"]
    config_file.close()
    return apiKey