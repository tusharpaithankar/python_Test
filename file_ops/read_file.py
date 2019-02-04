#File operations

#Read file containt at once

f1 = open("Test.txt", "r")  #open the file in write mode
print(f1.read())


#or we can read file one line by line as follows 

#Now here if i am not opening the file once again -> then the file pointer already read the complete file the the previous print and its pointing to end of file
#so there is nothing to read further and it wont print anything for next for loop  -> thats the reason opened file once again so that file pointer will point to
#start of file and can read the full file data once again with for loop.

f1 = open("Test.txt", "r")  #open the file in write mode
for data in f1:
    print(data)


#Print perticular number of char
f1 = open("Test.txt", "r")  #open the file in write mode
print(f1.read(3))           #enter number of char to be read and print 

