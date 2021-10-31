from .base import BaseEmbeddedDocument
from ..extensions import db


class PhoneCall(BaseEmbeddedDocument):

    id = db.UUIDField()
    length = db.IntField()
    sentiment = db.IntField()
    link = db.StringField()
    date = db.DateTimeField()
