from openai import OpenAI

client=OpenAI()

response=client.responses.create(
    model="gpt-4o",
    input="hii there" 
)

result=response.output_text
print("AI RESPONSE:",result)
