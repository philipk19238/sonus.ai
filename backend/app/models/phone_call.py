from .base import BaseEmbeddedDocument
from ..extensions import db

class PhoneCall(BaseEmbeddedDocument):

    id = db.UUIDField()
    length = db.IntField()
    sentiment = db.StringField()
    link = db.StringField() 
