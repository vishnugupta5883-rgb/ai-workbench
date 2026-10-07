import os
import sys
from dotenv import load_dotenv
from openai import OpenAI, AuthenticationError, APIConnectionError

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")

if not api_key:
    print("Error: OPENAI_API_KEY environment variable is not set.")
    sys.exit(1)

client = OpenAI(api_key=api_key)
MODEL = os.getenv("OPENAI_MODEL", "gpt-4.1-mini")

# -- call--
print("Sending prompt :'what is Generative AI in one sentence?'")

try:
    response = client.chat.completions.create(
        model=MODEL,
        messages=[
            {"role": "system", "content": "You are a helpful assistant. Be concise."},
            {"role": "user", "content": "what is Generative AI in one sentence?"},
        ],
        temperature=0.7,
        max_tokens=100        
    )

    # response + errors

    print("Response:", response.choices[0].message.content)
    print("Tokens used:", response.usage.total_tokens)

except AuthenticationError :
    print("Error: Invalid API key.Check your .env file. ")
except APIConnectionError:
    print("Error: Cannot connect.Check your internet connection.")
except Exception as e:
    print(f"Unexpected error: {e}")