"""The python module for the authentication handler functions."""

import json
import uuid
from typing import Any

import bcrypt
from models.user import User
from utils.utils import status_json


def register(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Register a new user."""
    body = json.loads(event["body"])
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(body["password"].encode("utf-8"), salt)
    try:
        user = User(
            hash_key=str(uuid.uuid4()),
            range_key=body["email"],
            first_name=body["first_name"],
            last_name=body["last_name"],
            hashed_password=hashed_password.decode("utf-8"),
            salt=salt.decode("utf-8")
        )
        user.save()
    except Exception as e:
        return status_json(500, {"message": str(e)})

    return status_json(200, {"message": "User created successfully."})
