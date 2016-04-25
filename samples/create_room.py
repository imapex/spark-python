from spark.rooms import Room
from spark.session import Session

token =  'YOUR TOKEN HERE'

url = 'https://api.ciscospark.com'

session = Session(url, token)

room = Room()
room.title = 'Spark-Python'
room.create(session)



