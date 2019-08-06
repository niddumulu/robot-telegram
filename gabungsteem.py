my_file = open("tekasli.txt", "r")
kata = my_file.read()
#print (kata)
my_file.close()

my_file2 = open("ekse.txt", "r")
kata2 = my_file2.read()
my_file.close()
kota = float(kata2)

if kota > 0:
   irit = ("JUAL ")
   urutanawal = (kata[0:93])
   uritan = (kata2[0:5])
   urutankedua = (kata[105:111])

   gabung = (irit+urutanawal+uritan+" STEEM "+urutankedua)

   gabungteks = gabung
   teks = format(gabungteks)
   file_nama = open("kirimeksekusi.txt","w")
   file_nama.write(teks)
   file_nama.close()
   
   simpan = gabung
   file_simpan = open("arsip.txt", "r+")
   teks = file_simpan.readlines()
   teks = format(simpan)+"\n"
   file_simpan.write(teks)
   file_simpan.close()
   
if kota == 0:
   print ("maaf")