import requests
import json

headers = {"content-type": "application/json"}
payload = json.dumps({ "name": "Apple AirPods", "data": { "color": "white", "generation": "3rd", "price": 135}})
requestUrl = "https://api.restful-api.dev/objects/ff808181923ed5e2019251c44f38283d"
r = requests.get(requestUrl, data=payload, headers=headers)

print(r.content)