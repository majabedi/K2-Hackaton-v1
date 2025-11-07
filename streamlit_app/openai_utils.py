import os
import openai

def get_openai_response(content: str) -> str:
    """
    Sends the given content to the OpenAI API and returns the response.

    The API key, base URL, and model are configured using environment variables:
    - OPENAI_API_KEY: Your OpenAI API key.
    - OPENAI_API_BASE: The base URL for the OpenAI API.
    - OPENAI_MODEL: The model to use for the completion.
    """
    api_key = os.getenv("OPENAI_API_KEY")
    base_url = os.getenv("OPENAI_API_BASE")
    model = os.getenv("OPENAI_MODEL")
    
    with open("prompt.txt", "r") as f:
        prompt = f.read()

    if not all([api_key, base_url, model]):
        raise ValueError("Missing one or more required environment variables: OPENAI_API_KEY, OPENAI_API_BASE, OPENAI_MODEL")

    client = openai.OpenAI(api_key=api_key, base_url=base_url)

    try:
        response = client.chat.completions.create(
            model=model,
            messages=[
                {"role": "system", "content": prompt},
                {"role": "user", "content": content},
            ],
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"An error occurred: {e}"
