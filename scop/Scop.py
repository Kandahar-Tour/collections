def myFunc():
    # local variable 
    name = "Mohammad"
    def myInnerFunc():
        print(name)
    myInnerFunc()

myFunc()


# global variable 
age = 21

def myAge():
    print("My age is :", age)

myAge()


class Show:
    def show(self):
        print(age)

t = Show()
print(t.show())