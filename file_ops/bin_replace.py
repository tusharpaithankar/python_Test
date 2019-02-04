#open and read the binary file data

f_bin = open("pic.PNG",'rb')

f_new = open("pic_changed.PNG",'wb')    #open the file to write in binary

for data in f_bin

