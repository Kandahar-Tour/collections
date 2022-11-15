from threading import*
from time import sleep
class Test:
    def odd(self):
        for i in range(5):
            if i % 2 == 1:
               print("odd number: " + str(i))
               sleep(1)

class Test1:
    def even(self):
        for i in range(5):
            if i % 2 == 0:
               print("even number: " + str(i))
               sleep(1)
obj1=Test()
obj2=Test1()
t1=Thread(target=obj1.odd)
t2=Thread(target=obj2.even)

t1.start()
t2.start()


t1.join()
t2.join()
print('Good by')
