from openai import OpenAI

client=OpenAI()

response=client.chat.completions.create(
    model="chatgpt-4o-latest",
    messages=[
        {"role":"system","content":"you are a chatbot"},
        {"role":"user","content":"hii who are you"}   
    ]
)

result= response.choices[0].message.content
print("AI RESPONSE:",result)

