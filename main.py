import time
import os

detik = int(0)
menit = int(0)

run = "passwde"
#print ("kirim")
while run.lower()=="passwde":
  if detik > 59 :
      detik = 0
      menit = menit+1
      if menit == 1 :
          from config import *
          client.send_message('cryptoindobot', '/r steem sbd') 
      if menit == 2 :
          from config import *
          for message in client.iter_messages('cryptoindobot', limit=1):
          print(utils.get_display_name(message.sender), message.message) 
      if menit == 15 :
          from config import *
          client.send_message('cryptoindobot', '/r steem sbd') 
      if menit == 16 :
          from config import *
           for message in client.iter_messages('cryptoindobot', limit=1):
          print(utils.get_display_name(message.sender), message.message)
      if menit > 29 :
         menit = -1
        
  #os.system('clear')
  detik = (detik+1)
  #print ("lihat")
  print ("menit :", menit,"detik : ",detik)
     
  time.sleep(1)
