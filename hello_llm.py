import os
from dotenv import load_dotenv
load_dotenv()

from openai import OpenAI
client = OpenAI(
    api_key=os.getenv("DEEPSEEK_API_KEY"),
    base_url="https://api.deepseek.com"
)

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "user", "content": "用一句话介绍你自己。"}
    ]
)

print(response.choices[0].message.content)
