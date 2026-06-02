from openai import OpenAI

client=OpenAI(
     api_key="GEMINI_API_KEY",
    base_url="https://generativelanguage.googleapis.com/v1beta/openai/"
    
)

response=client.chat.completions.create(
    model="gemini-2.0-flash",
    messages=[
        {"role":"user","content":"hii,there"}
    ]
    
)

print(response.choices[0].message.content)