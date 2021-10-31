from .base import BaseDocument
from .phone_call import PhoneCall
from ..extensions import db


class User(BaseDocument):

    id = db.UUIDField()
    phone_number = db.StringField()
    calls = db.EmbeddedDocumentListField(PhoneCall)
