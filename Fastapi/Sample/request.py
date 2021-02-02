import requests
import json

RUN_URL = 'http://127.0.0.1:8000/compile/'

data = {
"source":"hello",
"lang":"python",
"time_limit":5,
}
data=json.dumps(data)
r = requests.post(RUN_URL,data)
print(r.json())
