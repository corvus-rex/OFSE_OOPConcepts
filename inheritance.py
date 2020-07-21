class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printname(self):
        print(self.firstname, self.lastname)

class Student(Person):
    def __init__(self, fname, lname, year):
        super().__init__(fname, lname)
        self.graduationyear = year

    def printinfo(self):
        print(self.firstname, self.lastname, self.graduationyear)

foo = Person("Adrian", "Riadi")
foo.printname()

bar = Student("Adrian", "Riadi", 2019)
bar.printinfo()