from spark.rooms import Room
from spark.messages import Message
from spark.session import Session

token =  'YOUR TOKEN HERE'
roomname = 'YOUR ROOM NAME'

url = 'https://api.ciscospark.com'

session = Session(url, token)

message = Message()
room = Room.get(session, name=roomname)
message.text = 'test message from python sdk automated testing'
room.send_message(session, message)

