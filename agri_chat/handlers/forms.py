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


def get_form(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Get a form."""
    try:
        form = Form.get(hash_key=event["pathParameters"]["id"])
    except Form.DoesNotExist:
        return status_json({"message": "Form not found."}, 404)

    return status_json(form.attribute_values, 200)
