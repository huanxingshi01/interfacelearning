import json

import yaml

# params = json.load(open("data01.json", 'rb'))
# print(params)

params01 = yaml.safe_load(open('data.yaml', 'r', encoding='utf-8'))
print(params01)
print(type(params01))
