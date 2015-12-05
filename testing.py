from spark.messages import Message
from spark.rooms import Room
from spark.session import Session

import unittest
import json

# try:
#     from credentials import URL, LOGIN, PASSWORD
# except ImportError:
#     print
#     print 'To run live tests, please create a credentials.py file with the following variables filled in:'
#     print """
#     URL = ''
#     LOGIN = ''
#     PASSWORD = ''
#     """

TOKEN='NjdhMzY0YjEtYzlmZC00MjFhLWExN2QtOWQ2NDRiMjkwNzgxOGIyNWNlYTQtMzNk'
#Cloud ROom
#roomid = 'Y2lzY29zcGFyazovL3VzL1JPT00vNzA5MGNmMzAtOTdhMy0xMWU1LWIyNzAtZDM2ZWRmMzJlODMz'
#Private Testing Room
roomid = 'Y2lzY29zcGFyazovL3VzL1JPT00vMWNlZGFhYjAtOWI2OC0xMWU1LThlNTItMGI1MDFmMTM4ZjJm'
URL = 'https://api.ciscospark.com'

MAX_RANDOM_STRING_SIZE = 20

session = Session(TOKEN, URL)

print session.base_url


class TestPerson(unittest.TestCase):
    def test_get_self_info(self):
        resp = session.get('/people/me')
        print resp.text


class TestMessage(unittest.TestCase):
    def test_create_message(self):
        message = Message()
        message.set_roomId(roomid)
        message.set_text('test message from python sdk automated testing')
        session.post(message.get_url(), message.get_json())

        #TODO cleanup

    def test_get_messages(self):

        resp = session.get('/messages?roomId={}'.format(roomid))
        print resp.text
        ret = []
        for item in resp.json()['items']:
            a = Message.from_json(item)
            print a.get_text()
            ret.append(a)
        return ret


    def test_create_room(self):
        room = Room()
        room.set_title('kecorbin api created room')
        resp = session.post(room.get_url(), room.get_json())
        print resp



    # This is a valid test that generates too much noise for now

    # def test_reply_to_message(self):
    #     messages = self.test_get_messages()
    #     for message in messages:
    #         try:
    #             reply = Message()
    #             reply.set_roomId(message.get_roomId())
    #             reply.set_text('sdk received message {}'.format(message.get_text()))
    #             session.post(reply.get_url(), reply.get_json())
    #
    #         except UnicodeEncodeError:
    #             raise UnicodeEncodeError('Recieved Unicode error posting: {}'.format(reply))

#
# class PoapReadOnlyTests(unittest.TestCase):
#
#     @property
#     def session(self):
#         session = Session(URL, LOGIN, PASSWORD)
#         res = session.login()
#         return session
#
#     def test_create_server(self):
#         server = Server()
#         self.assertIsInstance(server, Server)
#
#     def test_get_servers(self):
#         servers = Server.get(self.session)
#         self.assertIsInstance(servers, list)
#         self.assertIsInstance(servers[0], Server)
#
#
#     def test_get_server_attributes(self):
#         servers = Server.get(self.session)
#         testserver = servers[0]
#
#         for method in dir(testserver):
#             if method.startswith('get_'):
#                 a = getattr(testserver, method)
#                 a()
#
#     def test_set_server_attributes(self):
#         servers = Server.get(self.session)
#         testserver = servers[0]
#
#         for method in dir(testserver):
#             if method.startswith('set_'):
#                 a = getattr(testserver, method)
#                 a('foo')


if __name__ == '__main__':
    offline = unittest.TestSuite()
  #  offline.addTest(dsfsdfasdkjf)

    online = unittest.TestSuite()
    online.addTest(TestMessage)
    # Add tests to this suite while developing the tests
    # This allows only these tests to be run
    # develop = unittest.TestSuite()
    #
    unittest.main(defaultTest='full')
