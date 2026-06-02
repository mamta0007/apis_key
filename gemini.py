from google import genai

client=genai.Client(
    api_key="GEMINI_API_KEY"
)

response=client.models.generate_content(
    model="gemini-2.0-flash",
    contents=["write the story about uvicorn"]
)

print("AI RESPONSE:",response.text)

