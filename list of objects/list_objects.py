class Test:
    def __init__(self, name, age):
        self.name = name 
        self.age = age

list = []
list.append(Test("Mansoor", 21))
list.append(Test("Ahmad", 22))
list.append(Test("Khan", 12))
list.append(Test("Faiz Mohammad",23))

for obj in list:
    print(obj.name, obj.age, sep= ' ')