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

    @classmethod
    def get_url(cls):
        return '/people'

    @classmethod
    def from_json(cls, obj):
        instance = cls(attributes=obj)
        return instance

    @classmethod
    def find(cls, session, name=None, email=None):
        """
        Retrieve a person by Display name or email
        :param session: Session object
        :return: person or list of person objects
        """
        if (name is None) and (email is None):
            raise ValueError('must specify either name or email')
        else:
            if name:
                query = 'displayName'
                value = name
            if email:
                query = 'email'
                value = email
            url = cls.get_url() + '?{}={}'.format(query, value)
            resp = session.get(url)
            items = json.loads(resp.text)['items']
            if len(items) == 1:
                obj = cls.from_json(items[0])
                ret = obj
            elif len(items) > 1:
                ret = []
                for i in items:
                    obj = cls.from_json(i)
                    ret.append(obj)
            return ret

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
