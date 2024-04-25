import requests
from translate import query

API_URL = "https://api-inference.huggingface.co/models/openai/whisper-large"
headers = {"Authorization": "Bearer XXXXX"}

def audio(filename):
    with open(filename, "rb") as f:
        data = f.read()
    response = requests.post(API_URL, headers=headers, data=data)
    return response.json()

output = audio("sample.flac")
data = query({"inputs":str(output),"parameters": {"src_lang": "en_XX", "tgt_lang": "fr_XX"}})
print(output)
print(data)

