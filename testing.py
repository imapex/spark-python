from spark.messages import Message
from spark.rooms import Room
from spark.session import Session
from spark.webhooks import Webhook
from spark.people import Person

import unittest
import json

try:
    from apitoken import TOKEN
except ImportError:
    print
    print('To run live tests, please create a apitoken.py file with the following variables filled in:')
    print("""
    TOKEN = '<YOUR API TOKEN>'

    """)

roomid = 'Y2lzY29zcGFyazovL3VzL1JPT00vMWNlZGFhYjAtOWI2OC0xMWU1LThlNTItMGI1MDFmMTM4ZjJm'
URL = 'https://api.ciscospark.com'

MAX_RANDOM_STRING_SIZE = 20

session = Session(URL, TOKEN)


class OfflineRoom(unittest.TestCase):

    testroom = {
                "id": "Y2lzY29zcGFyazovL3VzL1JPT00vYmJjZWIxYWQtNDNmMS0zYjU4LTkxNDctZjE0YmIwYzRkMTU0",
                "title": "Project Unicorn - Sprint 0",
                "sipAddress": "8675309@ciscospark.com",
                "created": "2015-10-18T14:26:16+00:00"
              }

    def test_0001_load_room_from_dict(self):

        obj = Room.from_json(self.testroom)
        self.assertIsInstance(obj, Room)

    def test_0002_load_room_from_str(self):
            data = json.dumps(self.testroom)
            obj = Room.from_json(data)
            self.assertIsInstance(obj, Room)


class OnlineRoom(unittest.TestCase):

    test_room_name = 'Python SDK Testing'

    def test_get_all_rooms(self):
        rooms = Room.get(session)
        self.assertIsInstance(rooms, list)
        self.assertTrue(len(rooms) > 1)

    def test_create_room(self):
        room = Room()
        room.set_title(self.test_room_name)
        resp = session.post(room.get_url(), room.get_json())
        print resp

    def test_get_room_by_name(self):
        room = Room.get(session, name=self.test_room_name)
        return self.assertIsInstance(room, Room)


class OnlinePeople(unittest.TestCase):
    def test_get_self_info(self):
        resp = session.get('/people/me')
        print resp.text

    def test_find_person_by_email(self):
        me = Person.find(session, name='John')
        self.assertIsInstance(me, list)
        self.assertTrue(len(me) > 1)


class OnlineWebook(unittest.TestCase):

    def test_create_webhook(self):
        webhook = Webhook()
        webhook.set_targetUrl('http://www.kevincorbin.net')


class OnlineMessages(unittest.TestCase):

    def test_create_message(self):
        message = Message()
        message.roomId = roomid
        message.text = 'test message from python sdk automated testing'
        session.post(message.get_url(), message.get_json())

    def test_get_messages(self):

        resp = session.get('/messages?roomId={}'.format(roomid))
        print resp.text
        ret = []
        for item in resp.json()['items']:
            a = Message.from_json(item)
            print a.text
            ret.append(a)
        return ret

    def test_reply_to_message(self):
        messages = self.test_get_messages()
        for message in messages:
            try:
                reply = Message()
                reply.roomId = message.roomId
                reply.text = 'sdk received message {}'.format(message.text)
                session.post(reply.get_url(), reply.get_json())

            except UnicodeEncodeError:
                raise UnicodeEncodeError('Recieved Unicode error posting: {}'.format(reply))

if __name__ == '__main__':
    offline = unittest.TestSuite()
    offline.addTest(OfflineRoom)
    online = unittest.TestSuite()
    online.addTest(OnlineMessages)
    online.addTest(OnlinePeople)
    online.addTest(OnlineRoom)
    online.addTest(OnlineWebook)

    full = unittest.TestSuite([online, offline])

    unittest.main(defaultTest='offline')