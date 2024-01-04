"""The python module for the form handler functions."""

import json
import uuid
from typing import Any

from models.form import Form


def create_form(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Create a new form."""
    body = json.loads(event["body"])

    form = Form(
        hash_key=uuid.uuid4().hex,
        user_email=body["user_email"],
        title=body["title"],
        text=body["text"]
    )
    form.save()

    return {
        "statusCode": 200,
        "body": json.dumps({
            "message": "Form created successfully."
        })
    }
