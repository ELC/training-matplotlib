"""Provide a safe gateway to import the adjacency lists"""

import json

def get_adj():
    with open('adjacency_lists.json', 'r') as jsonfile:
        json_data = jsonfile.read()
    return json.loads(json_data)