"""The user model."""

from datetime import datetime

from pynamodb.attributes import BooleanAttribute, MapAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class User(Model):
    """The user model."""

    class Meta:
        """The meta class."""

        table_name = "Users"
        region = "eu-west-1"

    email = UnicodeAttribute(hash_key=True)
    phone_number = UnicodeAttribute(null=True)
    first_name = UnicodeAttribute()
    last_name = UnicodeAttribute()
    hashed_password = UnicodeAttribute()
    salt = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=datetime.now)
    is_vip = BooleanAttribute(default=False)
    address = MapAttribute()
