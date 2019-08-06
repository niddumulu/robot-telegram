my_file = open("open.txt", "r")
kata = my_file.readlines()
banyakorder = (len(kata))
katak = kata.sort()
my_file.close()
      
data = [kata] 
with open("open.txt", "w") as txt_file: 
    for line in data:
         txt_file.write("".join(line) +"")