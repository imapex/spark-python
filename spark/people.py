import json

class Person(object):
    def __init__(self, attributes=None):
        if attributes:
            self.attributes = attributes
        else:
            self.attributes = dict()
            self.attributes['created'] = None
            self.attributes['displayName'] = None
            self.attributes['id'] = None
            self.attributes['avatar'] = None
            self.attributes['emails'] = None

    def set_created(self, val):
        self.attributes['created'] = val

    def get_created(self):
        return self.attributes['created']

    def set_displayName(self, val):
        self.attributes['displayName'] = val

    def get_displayName(self):
        return self.attributes['displayName']

    def set_id(self, val):
        self.attributes['id'] = val

    def get_id(self):
        return self.attributes['id']

    def set_avatar(self, val):
        self.attributes['avatar'] = val

    def get_avatar(self):
        return self.attributes['avatar']

    def set_emails(self, val):
        self.attributes['emails'] = val

    def get_emails(self):
        return self.attributes['emails']

    def get_json(self):
        return json.dumps(self.attributes)
