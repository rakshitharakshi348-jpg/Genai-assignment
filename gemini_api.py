from google import genai

client = genai.Client(api_key="YOUR_API_KEY")

prompt = input("Enter prompt: ")

response = client.models.generate_content(
    model="gemini-1.5-pro",
    contents=prompt
)

print(response.text)