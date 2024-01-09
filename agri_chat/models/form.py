"""The form model."""
import uuid
from datetime import datetime

from pynamodb.attributes import BooleanAttribute, ListAttribute, UnicodeAttribute, UTCDateTimeAttribute
from pynamodb.models import Model


class Form(Model):
    """The form model."""

    class Meta:
        """The meta class."""

        table_name = "Forms"
        region = "eu-west-1"

    id = UnicodeAttribute(hash_key=True, default=uuid.uuid4().hex)
    user_email = UnicodeAttribute()
    title = UnicodeAttribute()
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=datetime.now)


class FormComment(Model):
    """The form comment model."""

    class Meta:
        """The meta class."""

        table_name = "FormComments"
        region = "eu-west-1"

    user_email = UnicodeAttribute(hash_key=True)
    id = UnicodeAttribute(range_key=True, default=uuid.uuid4().hex)
    title = UnicodeAttribute()
    text = UnicodeAttribute()
    created_at = UTCDateTimeAttribute(default=datetime.now)
    is_edited = BooleanAttribute(default=False)
    tags = ListAttribute(null=True)
