import json


class Room(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['sipAddress'] = None
            self.attributes['created'] = None
            self.attributes['id'] = None
            self.attributes['title'] = None

    @staticmethod
    def get_url():
        return '/rooms'

    @classmethod
    def set_sipAddress(self, val):
        self.attributes['sipAddress'] = val

    def get_sipAddress(self):
        return self.attributes['sipAddress']

    def set_created(self, val):
        self.attributes['created'] = val

    def get_created(self):
        return self.attributes['created']

    def set_id(self, val):
        self.attributes['id'] = val

    def get_id(self):
        return self.attributes['id']

    def set_title(self, val):
        self.attributes['title'] = val

    def get_title(self):
        return self.attributes['title']

    def get_json(self):
        return json.dumps(self.attributes)
