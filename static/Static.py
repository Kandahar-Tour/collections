class Static:
    # static variable 
    i = 12
    name = 'Mohammad'

    # static method

    @staticmethod
    def show(self, name):
        return self.name

print(Static.i)