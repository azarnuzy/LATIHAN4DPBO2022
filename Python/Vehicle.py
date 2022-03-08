# kelas yang digunakan untuk mengimplementasikan Vehicle
# kelas Vehicle
class Vehicle:
    # private atribute dari kelas Vehicle
    __name = ""
    __fuelType = ""
    __maxPassengers = 0
    __age = 0

    def __init__(self, name="", fuelType="", maxPassengers=0, age=0):
        # konstruktor
        self.__name = name
        self.__fuelType = fuelType
        self.__maxPassengers = maxPassengers
        self.__age = age

    # mengeset nilai atribut name
    def setName(self, name):
        self.__name = name

    # mengembalikan nilai atribut name
    def getName(self):
        return self.__name

    # mengeset nilai atribut fuelType
    def setFuelType(self, fuelType):
        self.__fuelType = fuelType

    # mengembalikan nilai atribut fuelType
    def getFuelType(self):
        return self.__fuelType

    # mengeset nilai atribut maxPassengers
    def setMaxPassengers(self, maxPassengers):
        self.__maxPassengers = maxPassengers

    # mengembalikan nilai atribut maxPassengers
    def getMaxPassengers(self):
        return self.__maxPassengers

    # mengeset nilai atribut age
    def setAge(self, age):
        self.__age = age

    # mengembalikan nilai atribut age
    def getAge(self):
        return self.__age

    # method move
    def move(self):
        print("This " + self.getName() + "is moving")

    # menampilkan atribut Vehicle
    def printVehicle(self):
        print("Name: " + self.getName())
        print("Fuel Type: " + self.getFuelType())
        print("Max Passengers: " + str(self.getMaxPassengers()))
        print("Age: " + str(self.getAge()))
