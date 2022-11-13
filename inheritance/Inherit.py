class Person:
    def __init__(self, firstname, lastname):
        self.firstname = firstname
        self.lastname = lastname
    
    def printName(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, firstname, lastname):
        super().__init__(firstname, lastname)

obj = Student("Mansoor", "Faizi")

print(obj.printName())