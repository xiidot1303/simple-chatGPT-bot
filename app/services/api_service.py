import requests, json
from config import RAPID_API_KEY

url = "https://simple-chatgpt-api.p.rapidapi.com/ask"

headers = {
	"content-type": "application/json",
	"X-RapidAPI-Key": RAPID_API_KEY,
	"X-RapidAPI-Host": "simple-chatgpt-api.p.rapidapi.com"
}

def request_chat_gpt(text):
    payload = {"question": text}
    response = requests.request("POST", url, json=payload, headers=headers)
    return json.loads(response.content.decode())['answer']
