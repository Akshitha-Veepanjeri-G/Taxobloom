import os
from dotenv import load_dotenv
from openai import OpenAI

load_dotenv()

api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key) if (api_key and api_key != "your_openai_api_key_here") else None

def generate_flower_description(flower_name):
    if not client:
        return f"Educational profile for {flower_name}."

    prompt = f"""
    Give a short 5-6 line educational description of the flower: {flower_name}.
    Include:
    - Physical characteristics (color, size)
    - Habitat and where it grows
    - Traditional or medicinal use (if applicable)
    - A fun fact

    Keep the tone simple and understandable for students.
    """

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
