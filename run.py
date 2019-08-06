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
      os.system("python robotgabung.py")
    if minutes == 5:
      print ("sahil")
      minutes = 0
      
  #os.system('clear')
  seconds = (seconds+1)
  print (minutes," : ", seconds)
  time.sleep(1)
