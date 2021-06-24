#open and read the binary file data : edited for test purpose only

f_bin = open("pic.PNG",'rb')    #rb -> read data in binary format

print(f_bin.read())

f_bin.close()
