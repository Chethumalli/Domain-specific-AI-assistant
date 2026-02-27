import os
from groq import Groq
from dotenv import load_dotenv

load_dotenv()

api_key = os.getenv("GROQ_API_KEY")

if not api_key:
    raise ValueError("GROQ_API_KEY not found. Check your .env file.")

client = Groq(api_key=api_key)


def generate_response(prompt):
    try:
        chat_completion = client.chat.completions.create(
            messages=[
                {"role": "user", "content": prompt}
            ],
            model="llama-3.1-8b-instant",  # ✅ Fixed here
            temperature=0.7
        )

        return chat_completion.choices[0].message.content

    except Exception as e:
        return f"Groq API Error: {str(e)}"