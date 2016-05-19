# -*- coding: utf-8 -*-
import requests

data = dict(
    name='name',
    tags=['one', 'four']
)

# data = {
#     'name': 'name',
#     'tags-0': 'one',
#     'tags-1': 'two',
# }

url = 'http://127.0.0.1:5000/'

r = requests.post(url, json=data)
print(r.text)
