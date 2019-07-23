#Retrieving messages from a chat 
from config import *

for message in client.iter_messages('cryptoindobot', limit=1):
          print(utils.get_display_name(message.sender), message.message) 
