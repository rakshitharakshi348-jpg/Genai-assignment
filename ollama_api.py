import requests

prompt = input("Enter prompt: ")

response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": "llama3",
        "prompt": prompt,
        "stream": False
    }
)

data = response.json()

print("Full response:", data)

if "response" in data:
    print("\nAI Answer:")
    print(data["response"])
else:
    print("\nError from API:", data)