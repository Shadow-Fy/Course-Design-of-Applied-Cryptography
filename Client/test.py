import json
import requests
import tkinter as tk

def login():
    data = json.dumps(
        {
            'username': 'admin',
            'password': 'admin',
            'confirm_password': "admin"
        }
    )
    r = requests.post(
        f'http://127.0.0.1:8000/api/register',
        data=data
    )
    return r


r = login()
print(r.json())



