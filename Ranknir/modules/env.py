import json 

ENV_VARIABLES_LOCATION = "../Global/env.json"

def env_variable(key):
    with open(ENV_VARIABLES_LOCATION) as f:
        data = json.load(f)
    return data.get(key)