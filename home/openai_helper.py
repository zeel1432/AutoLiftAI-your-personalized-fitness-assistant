# chatapp/openai_helper.py

import openai
from django.conf import settings

openai.api_key = settings.OPENAI_API_KEY

def generate_response(prompt):
    response = openai.Completion.create(
        engine="text-davinci-003",  # Use the appropriate engine
        prompt=prompt,
        max_tokens=150,
        n=1,
        stop=None,
        temperature=0.7,
    )
    return response.choices[0].text.strip()
