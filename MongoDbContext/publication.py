from mongoengine import *


class Author(EmbeddedDocument):
    dataid = LongField(unique=True, name='i')
    name = StringField(required=True, name='n')
    order = IntField(required=True, name='r')


class Citation(EmbeddedDocument):
    publicationid = LongField(unique=True, name='i')
    raw = StringField(required=True, name='r')
    context = ListField(StringField(), name='c')


class Publication(Document):
    dataid = LongField(unique=True, name='i')
    title = StringField(name='t')
    abstract = StringField(name='b')
    content = StringField(required=True, name='c')
    venue = StringField(name='v')
    authors = EmbeddedDocumentListField(Author, name='a')
    citations = EmbeddedDocumentListField(Citation, name='s')
