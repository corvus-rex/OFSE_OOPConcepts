class Person:
    def __init__(self):
        self.first_name = 'Adrian' # this is a public attribute
        self.__last_name = 'Riadi' # this is a private attribute
    
    def printname(self): # public method
        return self.first_name + " " + self.__last_name
    
    def __greetings(self):
        return "Hello my name is " + self.first_name + self.__last_name

Adrianov = Person()
print(Adrianov.first_name)
print(Adrianov.printname())
# print(Adrianov.__last_name) # this will result in error
# print(Adrianov._Person__last_name) # calling a private variable by mangling
print(Adrianov.__greetings()) # this will result in error