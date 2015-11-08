from mongoengine import connect,StringField,Document,ListField,IntField

connect('test')

class TestModel(Document):
    testid = StringField(required=True)
    text = StringField(required=True)

class ZhihuModel(Document):
    item_id = IntField(required=True)
    item_date = StringField(required=True)
    item_title = StringField(required=True)
    item_content = StringField()
    item_css = StringField()
    item_frontimg = StringField(required=True)