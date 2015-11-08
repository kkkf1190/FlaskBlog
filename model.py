from mongoengine import connect,StringField,IntField,Document

connect('test')

class TestModel(Document):
    id = StringField(required=True)
    text = StringField(required=True)