#file operation  -> copying data from one file to another

f1 = open("Test.txt", "r")   #open first file in read mode from which we have to read the data and write the data into the another file (Open file in read mode)

f2 = open("Copied_file.txt", "w")   #open another file in which we have to copy the containt (open file in write mode)


x = f1.read()
b = f2.write(x) 
