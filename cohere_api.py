import cohere
import os
from dotenv import load_dotenv

load_dotenv()

co = cohere.Client(os.getenv("COHERE_API_KEY"))

prompt = input("Enter prompt: ")

response = co.generate(
model="command",
prompt=prompt,
max_tokens=200
)

print(response.generations[0].text)