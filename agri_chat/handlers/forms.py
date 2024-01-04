"""The python module for the form handler functions."""

import json
import uuid
from typing import Any

from models.form import Form
from utils.utils import get_token_data, status_json


def create_form(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Create a new form."""
    body = json.loads(event["body"])
    token_data = get_token_data(event["headers"]["Authorization"])
    form = Form(
        hash_key=uuid.uuid4().hex,
        user_email=token_data["email"],
        title=body["title"],
        text=body["text"]
    )
    form.save()

    return status_json({"message": "Form created successfully."}, 200)

