import json
import os

APP_ROOT = os.path.dirname(os.path.abspath(__file__))
FILEE = os.path.join(APP_ROOT, '', 'status.json')

def new_u():
    with open(FILEE, 'r') as f:
        data = json.load(f)
        data['new_users'] += 1
        data['total'] += 1
    with open(FILEE, 'w') as f:
        json.dump(data, f)

def new_f():
    with open(FILEE, 'r') as f:
        data = json.load(f)
        data['new_firms'] += 1
        data['total'] += 1
    with open(FILEE, 'w') as f:
        json.dump(data, f)

def c_log():
    with open(FILEE, 'r') as f:
        data = json.load(f)
        data['new_users'] = 0
        data['new_firms'] = 0
    with open(FILEE, 'w') as f:
        json.dump(data, f)


        