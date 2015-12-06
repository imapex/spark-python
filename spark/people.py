import json


class Person(object):
    def __init__(self, attributes=None):
        if attributes:
            self._attributes = attributes
        else:
            self._attributes = dict()
            self._attributes['created'] = None
            self._attributes['displayName'] = None
            self._attributes['id'] = None
            self._attributes['avatar'] = None
            self._attributes['emails'] = None

    @property
    def created(self):
        return self._attributes['created']


    @created.setter
    def created(self, val):
        self._attributes['created'] = val

    @property
    def displayName(self):
        return self._attributes['displayName']

    @displayName.setter
    def set_displayName(self, val):
        self._attributes['displayName'] = val

    @property
    def id(self):
        return self._attributes['id']

    @id.setter
    def set_id(self, val):
        self._attributes['id'] = val

    @property
    def avatar(self):
        return self._attributes['avatar']

    @avatar.setter
    def avatar(self, val):
        self._attributes['avatar'] = val

    @property
    def emails(self):
        return self._attributes['emails']

    @emails.setter
    def emails(self, val):
        self._attributes['emails'] = val

    def get_json(self):
        return json.dumps(self._attributes)


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