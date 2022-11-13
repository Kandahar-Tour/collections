class Test:
    __name = None
    __age = None
    def __init__(self, name, age):
        self.__name = name
        self.__age = age
    

    def __str__(self):
        return (f"Name: {self.__name} \nAge: {self.__age}")

print(Test("Mansoor", 21))