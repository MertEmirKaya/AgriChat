"""The message model for chat-gpt messages."""

from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class Message(Model):
    """The message model."""

    class Meta:
        """The meta class."""

        table_name = "Messages"
        region = "eu-west-1"

    id = UnicodeAttribute(hash_key=True)
    owner = UnicodeAttribute(range_key=True) # either user email or "bot"
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=datetime.now)
