"""The python module for the form handler functions."""

import json
import uuid
from typing import Any

from models.form import Form
from pynamodb_encoder.encoder import Encoder
from utils.utils import get_token_data, status_json


def create_form(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Create a new form."""
    body = json.loads(event["body"])
    token_data = get_token_data(event["headers"]["Authorization"])
    encoder = Encoder()
    form = Form(
        hash_key=uuid.uuid4().hex,
        user_email=token_data["email"],
        title=body["title"],
        text=body["text"]
    )
    form.save()

    return status_json(encoder.encode(form), 200)


def get_form(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Get a form."""
    encoder = Encoder()
    try:
        form = Form.get(hash_key=event["pathParameters"]["id"])
    except Form.DoesNotExist:
        return status_json({"message": "Form not found."}, 404)

    return status_json(encoder.encode(form), 200)


def list_forms(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """List all forms."""
    forms = Form.scan()
    encoder = Encoder()
    forms_list = [encoder.encode(item) for item in forms]
    return status_json({"result": forms_list, "count": forms.total_count}, 200)


def delete_form(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Delete a form."""
    try:
        form = Form.get(hash_key=event["pathParameters"]["id"])
    except Form.DoesNotExist:
        return status_json({"message": "Form not found."}, 404)

    token_data = get_token_data(event["headers"]["Authorization"])
    if form.user_email != token_data["email"]:
        return status_json({"message": "You are not authorized to delete this form."}, 401)

    form.delete()
    return status_json({"message": "Form deleted."}, 200)


def update_form(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Update a form."""
    try:
        form = Form.get(hash_key=event["pathParameters"]["id"])
    except Form.DoesNotExist:
        return status_json({"message": "Form not found."}, 404)

    token_data = get_token_data(event["headers"]["Authorization"])
    if form.user_email != token_data["email"]:
        return status_json({"message": "You are not authorized to update this form."}, 401)

    encoder = Encoder()
    body = json.loads(event["body"])
    for key, value in body.items():
        if key != "id" and key != "user_email" and key != "created_at":
            continue

        setattr(form, key, value)

    form.save()
    return status_json(encoder.encode(form), 200)
