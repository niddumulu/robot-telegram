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
          from kirim import *
          
      if menit == 2 :
          from pesan import *
           
      if menit == 15 :
          from kirim import *
          
      if menit == 16 :
          from pesan import *
           
      if menit > 29 :
         menit = -1
        
  #os.system('clear')
  detik = (detik+1)
  #print ("lihat")
  print ("menit :", menit,"detik : ",detik)
     
  time.sleep(1)
