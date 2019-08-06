#robot2 menenetukan jual beli
import time
import os
import string
from otak import *

my_file = open("kirimeksekusi.txt", "r")
kata = my_file.read()
my_file.close()
pesand = kata
#print (pesand)
pesan = pesand[0:4]
#print (pesan)
pesanno = pesand[5:116]
#print (pesanno)
pesanho = ("import os"+"\n"+pesanno)
#print (pesanho)
#print (pesan)
if pesan == 'JUAL':
             print ("kirim")
             teks = format(pesanho)
             file_nama = open("jualbeli.py","w")
             file_nama.write(teks)
             file_nama.close()
             from jualbeli import *
             from kosongkan import *
       

if pesan == 'HOLD':
             print ("hold")