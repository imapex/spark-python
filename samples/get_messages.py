from spark.rooms import Room
from spark.session import Session

token =  'YOUR TOKEN HERE'
roomname = 'YOUR ROOM NAME'

url = 'https://api.ciscospark.com'

session = Session(url, token)

room = Room.get(session, name=roomname)
msgs = room.get_messages(session)
print 'get messages from room {}'.format(room.title)
for msg in msgs:
    print msg.text
