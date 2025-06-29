class Car:                            #Not that class name should be start from Capital letter

    total_car = 0

    @staticmethod        # this is call dacorators
    def general_description():      #static method      # here also see that no need to use "self" keyword
        return "cars are amazing!"

    def __init__(self,b,m): # constructor                 # in othet language we use "this" keyword here we use "self" keyword
        self.__brand = b           # whenever we devlare variable with "__" now it will private only that class methods can access that veriable
        self.__model = m
        Car.total_car += 1

    def get_brand(self):
        return self.__brand

    def set_brand(self,b):
        self.__brand = b

    def fullname(self):
        return f"{self.__brand} {self.__model}"

    def fuel_type(self):   #Polymorphism
        return "Petrol or diesel"
    
    @property        # this will make sure that we can not change this variable
    def model(self):
        return self.__model



class Electriccar(Car): # inheritance
    def __init__(self,b,m,bs):
        super().__init__(b,m)
        self.batterysize = bs

    def carDetail(self):
        return f"{super().get_brand()}  {self.model}  {self.batterysize}"
    
    def fuel_type(self):     #Polymorphism
        return "Electric Charge"


myCar1Object = Car("Toyota", "Corolla")
# print(myCar1Object.brand)
print(myCar1Object.model)
print(myCar1Object.fullname())


myCar2Object = Car("Tata", "Safari")
# print(myCar2Object.brand)
print(myCar2Object.model)
print(myCar2Object.fullname())


Tesla = Electriccar("Tesla", "Model S", "35")
print(Tesla.fullname())
print(Tesla.carDetail())
# print(Tesla.brand)
print(Tesla.get_brand())
Tesla.set_brand("Spacex")
print(Tesla.get_brand())

print(Tesla.fuel_type())
print(myCar1Object.fuel_type())


print(Car.total_car)

# print(Tesla.general_description())          # error because this is static methods
print(Car.general_description())

Tesla.__model = "osjbk"
print(Tesla.carDetail())



print(isinstance(Tesla,Car))
print(isinstance(Tesla,Electriccar))
print(isinstance(myCar1Object,Electriccar))


class Battery:
    def battery_info(self):
        return "This is battery"

class Engine:
    def engine_info(self):
        return "This is engine"


class ElectricCarTwo(Battery,Engine,Car):
    pass


myNewTesla = ElectricCarTwo("Tesla2", "Model ss")
print(myNewTesla.engine_info())
print(myNewTesla.battery_info())