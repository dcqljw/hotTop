import mongoengine
from django.db import models


class HotTop(mongoengine.Document):
    idx = mongoengine.IntField()
    title = mongoengine.StringField()
    url = mongoengine.StringField()
    date = mongoengine.StringField()
    source = mongoengine.StringField()

    meta = {'collection': "HotTop"}
