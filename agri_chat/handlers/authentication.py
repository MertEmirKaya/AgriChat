"""The python module for the authentication handler functions."""

import datetime
import json
import os
from typing import Any

import bcrypt
import jwt
from models.user import User
from utils.utils import status_json


def register(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Register a new user."""
    body = json.loads(event["body"])
    salt = bcrypt.gensalt()
    hashed_password = bcrypt.hashpw(body["password"].encode("utf-8"), salt)

    user = User(
        hash_key=body["email"],
        first_name=body["first_name"],
        last_name=body["last_name"],
        hashed_password=hashed_password.decode("utf-8"),
        salt=salt.decode("utf-8")
    )
    user.save()

    return status_json({"message": "User created successfully."}, 200)


def login(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Login a user."""
    body = json.loads(event["body"])
    try:
        user = User.get(hash_key=body["email"])
    except User.DoesNotExist:
        return status_json({"message": "Either your email or password is incorrect."}, 401)

    entered_password = body.get("password", "").encode("utf-8")
    hashed_password = bcrypt.hashpw(entered_password, user.salt.encode("utf-8")).decode("utf-8")
    if hashed_password == user.hashed_password:
        expiration_time = datetime.datetime.utcnow() + datetime.timedelta(hours=1)

        payload = {
            "email": user.email,
            "first_name": user.first_name,
            "last_name": user.last_name,
            "exp": expiration_time,
        }

        token = jwt.encode(payload, os.environ["SECRET_KEY"], algorithm="HS256")
        return status_json({"token": token}, 200)

    else:
        return status_json({"message": "Either your email or password is incorrect"}, 401)
