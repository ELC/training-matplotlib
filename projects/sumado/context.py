"""Provide a safe gateway to import the adjacency lists"""

import json
import os.path


def get_adj_list(adj_id):
    scriptpath = os.path.dirname(__file__)
    filename = os.path.join(scriptpath, 'adjacency_lists.json')
    with open(filename, 'r') as jsonfile:
        json_data = jsonfile.read()
    adj_lists = json.loads(json_data)
    adj_list = adj_lists[adj_id]
    adj_list_converted = {int(i):j for i,j in adj_list.items()}
    return adj_list_converted