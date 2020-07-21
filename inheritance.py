class Person:
    def __init__(self):
        self._firstname = None
        self._lastname = None

    def printname(self):
        print(self._firstname, self._lastname)
    
    @property
    def firstname(self):
        print("getter of firstname called")
        return self._firstname

    @firstname.setter
    def firstname(self, value):
        print("setter of firstname called")
        self._firstname = value

    @property
    def lastname(self):
        print("getter of lastname called")
        return self._lastname

    @lastname.setter
    def lastname(self, value):
        print("setter of lastname called")
        self._lastname = value

class Student(Person):
    def __init__(self):
        super().__init__()
        self._graduationyear = None
    
    @property
    def graduationyear(self):
        print("getter of graduationyear called")
        return self._graduationyear

    @graduationyear.setter
    def graduationyear(self, value):
        print("setter of graduationyear called")
        self._graduationyear = value

    def printinfo(self):
        print(self._firstname, self._lastname, self._graduationyear)

foo = Person()
foo.firstname = "Adrian"
foo.lastname = "Riadi"
print(foo.firstname)
print(foo.lastname)
foo.printname()

bar = Student()
bar.firstname = "Adrian"
bar.lastname = "Riadi"
bar.graduationyear = 2019
bar.printinfo()