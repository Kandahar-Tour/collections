from threading import*
from time import sleep
class Test:
    def print_hello(self):
        for i in range(5):
            print('hello')
            sleep(1)

class Test1:
    def print_hi(self):
        for i in range(5):
            print('Hi')
            sleep(1)
obj1=Test()
obj2=Test1()
t1=Thread(target=obj1.print_hello,args=())
t2=Thread(target=obj2.print_hi,args=())

t1.start()
sleep(0.2)
t2.start()


t1.join()
t2.join()
print('bye')
# there we have three threads 1 main thread , thread 1 and thread 2 there the main is printing between two other threads 
#if we want to first do other threads and in the final we do the main thread we use join