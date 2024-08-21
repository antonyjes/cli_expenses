import json
import datetime

def load_json(filename):
    with open(filename, 'r') as file:
        return json.load(file)

def save_json(filename, data):
    with open(filename, 'w') as file:
        json.dump(data, file, indent=2)

def date_format(date):
    return datetime.datetime.strptime(date, '%Y-%m-%d')