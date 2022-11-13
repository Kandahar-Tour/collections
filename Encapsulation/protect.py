class Test:
    def __init__(self):
        self.name = "Ahmad"
        self.__name = "Mansoor"
    

class Test1(Test):
    def __init__(self):
        
        # calling constructor of Test class 
        Test.__init__(self)
        print("Collecting private member of base class: ")
        print(self.__name)


obj = Test()

print(obj.name)