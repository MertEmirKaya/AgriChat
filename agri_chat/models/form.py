"""The form model."""

from datetime import datetime

from pynamodb.attributes import UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class Form(Model):
    """The form model."""

    class Meta:
        """The meta class."""

        table_name = "Forms"
        region = "eu-west-1"

    id = UnicodeAttribute(hash_key=True)
    user_email = UnicodeAttribute()
    title = UnicodeAttribute()
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=datetime.now)
