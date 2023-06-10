import json
import os

modules = [file for file in os.listdir("v2/modules") if file.endswith('.json')]
for file in modules:   
    with open('v2/modules/{}'.format(file), "r") as getJson:
        data = json.load(getJson)
    print(data["moduleName"])
print(modules)