import os
import openai
openai.api_key = os.getenv("OPENAI_API_KEY")

user_input = input("Please enter your prompt: ")

completion = openai.ChatCompletion.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": user_input}
  ],
  temperature=0.2,
  max_tokens=100
)

print(completion.choices[0].message)
 
