import requests

url = 'http://127.0.0.1:8000/api/endpoint/'
data = {'username': '1', '2': '3'}

response = requests.post(url, json=data)

if response.status_code == 200:
    print('请求成功')
else:
    print('请求失败:', response.status_code)
