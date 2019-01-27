#This is demonstration of parallal execution
#Two class Hello and Hi - which is running in serial - as both the class is running by the main thread.

class hello: 
        def run(self):
            for i in range (5):
                print("Hello")


class hi:
        def run(self):
            for i in range (5):
                print("Hi")
t1 = hello() 
t2 = hi() 

t1.run()
t2.run()
