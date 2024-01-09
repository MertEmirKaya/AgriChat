"""The Module contains the chat_gpt handler function."""

import os
from typing import Any

from models.message import Message
from openai import OpenAI
from utils.utils import get_token_data, status_json


def chat_gpt(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Get the message from the query string and return the response from GPT-3."""
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))
    content = event["queryStringParameters"].get("message")
    if not content:
        return status_json({"message": "No message provided", "status": 400})

    token_data = get_token_data(event["headers"]["Authorization"])
    message = Message(owner=token_data["email"], text=content)
    message.save()
    completion = client.chat.completions.create(
        messages=[
            {
                "role": "user",
                "content": content,
            }
        ],
        model="gpt-3.5-turbo-1106"
    )
    bot_message = Message(owner=token_data["email"], text=completion.choices[0].message.content, bot=True)
    bot_message.save()

    return status_json({"message": completion.choices[0].message.content, "status": 200})


def get_history_gpt(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Get the message history for the user."""
    token_data = get_token_data(event["headers"]["Authorization"])
    messages = Message.query(token_data["email"])
    return status_json({"messages": [message.text for message in messages], "status": 200})
