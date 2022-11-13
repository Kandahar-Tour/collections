class Test:
    _name = 'Mansoor'

class Test1(Test):
    def __str__(self):
        return self._name

print(Test1())