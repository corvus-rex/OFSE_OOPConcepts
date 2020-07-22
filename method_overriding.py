class Automobile:
    def __init__(self, color, manufacturer, wheels):
        self._color = color
        self._manufacturer = manufacturer
        self._wheels = wheels
        # self.__wheels = wheels # private attribute will not be inherited to child
    
    @property
    def color(self):
        return self._color
    
    @property
    def manufacturer(self):
        return self._manufacturer
    
    @property
    def wheels(self):
        return self._wheels

class Sedan(Automobile):
    def __init__(self, color, manufacturer):
        super().__init__(color, manufacturer, 4)
    
    @property
    def wheels(self):
        print("Method is overriden")
        return self._wheels

Truck_1 = Automobile('red', 'Volvo', 6)
print(Truck_1.wheels)

Sedan_1 = Sedan('blue', 'Honda')
print(Sedan_1.wheels)