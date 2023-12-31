"""Utility functions for the agri_chat application."""

import json
from typing import Any


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
