import json


def get_var(name: str):
    file = open("../../config.json", "r")
    vars = json.load(file)
    file.close()
    var = vars[name]
    return var
# do error handling for this