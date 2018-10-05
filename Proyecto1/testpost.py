import requests
import json

data = {
    "id": 1, 
    "subject": "your-email@your-domain.com", 
    "predicate": "Mac",
    "object": "private airplanes are a rich man's toy 2",
    "translate": "mi traducion"
}

data_json = json.dumps(data)

headers = {'Content-type': 'application/json'}

response = requests.post('http://127.0.0.1:4567/addtranslate', data=data_json, headers=headers)

print(response)