"""Provide a safe gateway to import the adjacency lists"""

import json
import os.path


def get_adj_list_by_id(adj_id):
    update()
    global adj_lists
    adj_list = adj_lists[adj_id]
    adj_list = {int(i): j for i, j in adj_list.items()}
    return adj_list


def add_adj_list(adj_id, adj_dict):
    update()
    global adj_lists
    if adj_id in adj_lists:
        return
    adj_lists[adj_id] = adj_dict
    global adjfile
    with open(adjfile, 'w') as jsonfile:
        json.dump(adj_stored, jsonfile)


def del_adj_list(adj_id):
    update()
    if adj_id not in adj_lists:
        return
    del adj_lists[adj_id]


def update():
    global adj_lists
    global adjfile
    scriptpath = os.path.dirname(__file__)
    adjfile = os.path.join(scriptpath, 'adjacency_lists.json')
    with open(adjfile, 'r') as jsonfile:
        json_data = jsonfile.read()
    adj_lists = json.loads(json_data)

adj_lists = None
adjfile = None
