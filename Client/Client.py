import json
import requests

def login():
    data = json.dumps(
        {
            'username': 'admin',
            'password': 'admin'
        }
    )
    r = requests.post(
        f'http://127.0.0.1:8000/api/login',
        data=data
    )
    return r
