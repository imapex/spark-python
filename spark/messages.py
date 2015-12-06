import json


class Message(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['text'] = None
            self.attributes['roomId'] = None

    def set_text(self, val):
        self.attributes['text'] = val

    def get_text(self):
        return self.attributes['text']

    def set_roomId(self, val):
        self.attributes['roomId'] = val

    def get_roomId(self):
        return self.attributes['roomId']

    def get_json(self):
        return json.dumps(self.attributes)

    @classmethod
    def get_url(cls):
        return '/messages'

    @classmethod
    def from_json(cls, obj):
        instance = cls(attributes=obj)
        return instance
