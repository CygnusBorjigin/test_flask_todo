import json
import os


def get_var(name: str):
    file = open("./config.json", "r")
    vars = json.load(file)
    file.close()

    # here = os.path.dirname(os.path.abspath(__file__))
    # filename = os.path.join(here, 'config.json')
    #


    return vars[name]
# do error handling for z
