#hapusbaris

my_file = open("open.txt", "r")
kata = my_file.readlines()
del (kata[0])
my_file.close()
      
data = [kata] 
with open("open.txt", "w") as txt_file: 
    for line in data:
         txt_file.write("".join(line) +"")