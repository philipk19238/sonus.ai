from ..extensions import db


class CrudMixin:

    @classmethod
    def create(cls, **kwargs):
        kwargs = {k: v for k, v in kwargs.items() if hasattr(cls,  k)}
        dao = cls(**kwargs)
        return dao

    def delete(self):
        self.delete()


class BaseDocument(db.Document, CrudMixin):
    meta = {'abstract': True}

    @classmethod
    def create(cls, **kwargs):
        dao = super(BaseDocument, cls).create(**kwargs)
        dao.save()
        return dao


class BaseEmbeddedDocument(db.EmbeddedDocument, CrudMixin):

    meta = {'allow_inheritance': True}
