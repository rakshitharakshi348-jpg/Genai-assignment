import requests
import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("HUGGINGFACE_API_KEY")

API_URL = "https://api-inference.huggingface.co/models/google/flan-t5-base"

headers = {
    "Authorization": f"Bearer {API_KEY}"
}

prompt = input("Enter prompt: ")

payload = {
    "inputs": prompt
}

response = requests.post(API_URL, headers=headers, json=payload)

print("Status:", response.status_code)

if response.status_code == 200:
    result = response.json()
    print(result)
else:
    print(response.text)