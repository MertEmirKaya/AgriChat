"""The Module contains the chat_gpt handler function."""

import os
from typing import Any

from openai import OpenAI
from utils.utils import status_json


def chat_gpt(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Get the message from the query string and return the response from GPT-3."""
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    content = event["queryStringParameters"].get("message")
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo-1106"
    )
    return status_json({"message": completion.choices[0].message.content, "status": "success"})
