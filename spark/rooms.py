import json
import spark.messages


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

    def __str__(self):
        return self.attributes['title']

    @classmethod
    def get_url(cls):
        return '/rooms'

    @classmethod
    def get(cls, session, name=None):
        """
        Retrieve room list
        :param session: Session object
        :return: list rooms available in the current session
        """
        ret = []
        rooms = json.loads(session.get(cls.get_url()).text)['items']
        for room in rooms:
            obj = cls.from_json(room)
            if name == obj.get_title():
                return obj
            else:
                ret.append(obj)
        return ret

    @classmethod
    def from_json(cls, obj):
        if isinstance(obj, dict):
            obj = cls(attributes=obj)
        elif isinstance(obj, (str, unicode)):
            obj = cls(attributes=json.loads(obj))
        else:
            raise TypeError('Data must be str or dict')
        return obj

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

    def send_message(self, session, msg):
        if isinstance(msg, spark.messages.Message):
            message = msg
        else:
            message = spark.messages.Message()
            message.set_text(msg)
        message.set_roomId(self.get_id())
        resp = session.post('/messages', message.get_json())
        return resp
