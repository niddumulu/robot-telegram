from config import *
import time
import os

seconds = int(0)
minutes = int(0)

run = "dia"
while run.lower()=="dia":
  if seconds == 59:
    seconds = 0
    minutes = minutes+1
    if minutes == 1:
      print ("saheu")
      client.send_message('steemsbd', '/r steem sbd')
    if minutes == 2:
      for message in client.iter_messages('steemsbd', limit=1):
         print(utils.get_display_name(message.sender), message.message)
         pecah = (message.message)
         simpan = pecah[78:84]
         file_simpan = open("data.txt", "r+")
         teks = file_simpan.readlines()
         teks = format(simpan)+"\n"
         file_simpan.write(teks)
         file_simpan.close()
      
    if minutes == 7:
      minutes = 0
  #os.system('clear')
  seconds = (seconds+1)
  print (minutes," : ", seconds)
  time.sleep(.1)



   #for message in client.iter_messages('steemsbd', limit=1):
         #print(utils.get_display_name(message.sender), message.message)
         #pecah = (message.message)
         #simpan = pecah[78:84]
         #file_simpan = open("data.txt", "r+")
         #teks = file_simpan.readlines()
         #teks = format(simpan)+"\n"
         #file_simpan.write(teks)
         #file_simpan.close()
