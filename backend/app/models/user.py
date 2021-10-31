from .base import BaseEmbeddedDocument
from .phone_call import PhoneCall
from ..extensions import db

class User(BaseEmbeddedDocument):

    id = db.UUIDField()
    phone_number = db.StringField()
    calls = db.EmbeddedDocumentField(PhoneCall)