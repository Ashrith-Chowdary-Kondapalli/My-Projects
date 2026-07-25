from openai import OpenAI

userprompt = input("Enter your prompt: ")
systemprompt = "Be strict"

response = OpenAI().responses.create(
    input=userprompt,
    model="gpt-4o-mini",
    instructions=systemprompt,
)   

print(response.output_text)