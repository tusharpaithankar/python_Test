#This is demonstration of parallal execution
#Now to run both the classes in parallal we have to bring thread in picture.
#it would be as follows

#1. Make both the class as thread.
#2. After declering the class as thread it will pop up error that the thread is something which is not defined.
#3. Now we have to define the thread by adding the system default library as follows (adding packages)
#4. even after this step you run the script it wont work as parallal
#5. Now we have to invoke the class using start (t1.start) -> though the class are defined in run -> we are invoking it using start as start in tern invoke the run class.
#6.     Here start will create two threads
# Thats how we can see two different threads running in parallel.
#---------------------------------
# 1. Now we have added speed in the one thread
# 2. sleep(1)   -> Need to add package before this
# 3. Now here the main thread will be exit before compete execution of thread 1 and 2 
# 4. in order to main thread wait to execute the created thread join has to use as follows


from threading import *                          #importing everything from the threading package
from time import sleep                           # importing the sleep from time package

class hello(Thread):                             #making class as the thread
        def run(self):
            for i in range (5):
                print("Hello")
                sleep(1)                         #sleep of 1sec


class hi(Thread):                                #making class as the thread.
        def run(self):
            for i in range (5):
                print("Hi")

t1 = hello() 
t2 = hi() 

t1.start()
t2.start()


t1.join()                                        #wait till t1 and t2 join
t2.join()

print ("Bye")                                    #bye will be printed by in thread

