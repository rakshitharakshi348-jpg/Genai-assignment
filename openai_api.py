import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def query_openai(prompt):
    try:
        response = client.chat.completions.create(
            model="gpt-4.1-mini",
            messages=[{"role": "user", "content": prompt}]
        )

        return response.choices[0].message.content

    except Exception as e:
        return str(e)

prompt = input("Enter prompt: ")
print(query_openai(prompt))