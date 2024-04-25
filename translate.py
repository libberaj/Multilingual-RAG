


import json
import requests

headers = {"Authorization": "Bearer hf_WhvcSHfBqMEYYTajxyXPWMZOmVjWSxUPM"}
API_URL = "https://api-inference.huggingface.co/pipeline/translation/facebook/mbart-large-50-many-to-many-mmt"


def query(payload):
    data = json.dumps(payload)
    response = requests.request("POST", API_URL, headers=headers, data=data)
    return json.loads(response.content.decode("utf-8"))
data = query({"inputs": "My name is Sarah Jessica Parker but you can call me Jessica", "parameters": {"src_lang": "en_XX", "tgt_lang": "fr_XX"}})

print(data)