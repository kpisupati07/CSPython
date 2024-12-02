class Car:
    def __init__(self, mpg, gallons):
        self.__mpg = mpg
        self.__gallons = gallons
        self.__current = 0
    def get_gas_level(self):
        return self.__current
    def add_gas(self, amount):
        if self.__current + amount > self.__gallons:
            print('exceeds max')
        else:
            self.__current += amount
    def drive(self, distance):
        if (self.__current * self.__mpg) < distance:
            print('not enough gas')
        else:
            self.__current -= distance/self.__mpg
            return self.get_gas_level()

my_hybrid = Car(50, 20) #50 miles per gallon
my_hybrid.add_gas(14) #Tank now has 14 gallons of gas
my_hybrid.drive(100) #Drive 100 miles
print (my_hybrid.get_gas_level(), "gallons of gas remain")