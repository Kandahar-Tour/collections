from abc import ABC, abstractclassmethod

class Polygon(ABC):
    @abstractclassmethod
    def show(self):
        pass
    
class Triangle(Polygon):
    def show(self):
        print("I have three sides")

obj = Triangle()
obj.show()

