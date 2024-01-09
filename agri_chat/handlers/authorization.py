"""The authorizer handler function."""

import os
from typing import Any

import jwt


def authorizer(event:dict[str, Any], context:dict[str, Any]) -> dict[str, Any]:
    """Authroize a user to access the API."""
    token = event['authorizationToken']

    # Validate and decode the JWT
    try:
        decoded_payload = jwt.decode(token, os.environ["SECRET_KEY"], algorithms=["HS256"])

        return {
            'principalId': 'user',
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [{
                    'Action': 'execute-api:Invoke',
                    'Effect': 'Allow',
                    'Resource': event['methodArn']
                }]
            },
            'context': {
                'user': decoded_payload
            }
        }
    except jwt.ExpiredSignatureError:
        # Token has expired
        return {
            'principalId': 'user',
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [{
                    'Effect': 'Deny',
                    'Resource': event['methodArn']
                }]
            }
        }
    except jwt.InvalidTokenError:
        # Invalid token
        return {
            'principalId': 'user',
            'policyDocument': {
                'Version': '2012-10-17',
                'Statement': [{
                    'Effect': 'Deny',
                    'Resource': event['methodArn']
                }]
            }
        }
