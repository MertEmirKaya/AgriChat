"""The message model for chat-gpt messages."""

import uuid
from datetime import datetime

from pynamodb.attributes import BooleanAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class Message(Model):
    """The message model."""

    class Meta:
        """The meta class."""

        table_name = "Messages"
        region = "eu-west-1"

    owner = UnicodeAttribute(hash_key=True)
    id = UnicodeAttribute(range_key=True, default=uuid.uuid4().hex)
    bot = BooleanAttribute(null=True, default=False)
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=datetime.now)
