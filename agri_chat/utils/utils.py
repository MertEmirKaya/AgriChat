"""Utility functions for the agri_chat application."""

import json
import os
from typing import Any

import jwt


def status_json(
    body: dict[str, Any], status_code: int = 200, content_type: str = "application/json"
) -> dict[str, Any]:
    """Return a response object with the given body and status code."""
    return {
        "statusCode": status_code,
        "headers": {
            "Content-Yype": content_type,
            "Access-Control-Allow-Methods": "*",
            "Access-Control-Allow-Headers": "*",
            "Access-Control-Allow-Origin": "*",
        },
        "body": json.dumps(body),
    }


def get_token_data(token: str) -> dict[str, Any]:
    """Return the token data from the given token."""
    payload = jwt.decode(token, key=os.environ["SECRET_KEY"], algorithms=['HS256'])
    print(payload)
    return payload
