#robot1, mendapatkan daftar harga
from configrobot1 import *
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
      print ("sahal")
      client.send_message('cryptoindobot', '/r steem sbd')
    if minutes == 2:
      for message in client.iter_messages('cryptoindobot', limit=1):
         print(utils.get_display_name(message.sender), message.message)
         pecah = (message.message)
         simpan = pecah[78:84]
         
         opena = simpan
         teks = format(opena)
         file_nama = open("hargasekarang.txt","w")
         file_nama.write(teks)
         file_nama.close()
         
    if minutes == 5:
      minutes = 0
  os.system('clear')
  seconds = (seconds+1)
  print (minutes," : ", seconds)
  time.sleep(1)