# Import kelas Vehicle
from Vehicle import Vehicle

# kelas yang digunakan untuk mengimplementasikan Ship
# kelas Ship


class Ship(Vehicle):
    # private atribute dari kelas Ship
    __type = ""
    __countryOfManufacture = ""

    def __init__(self, type="", countryOfManufacture=""):
        # konstruktor
        super().__init__()
        self.__type = type
        self.__countryOfManufacture = countryOfManufacture

    # mengeset nilai atribut type
    def setType(self, type):
        self.__type = type

    # mengembalikan nilai atribut type
    def getType(self):
        return self.__type

    # mengeset nilai atribut countryOfManufacture
    def setCountryOfManufacture(self, countryOfManufacture):
        self.__countryOfManufacture = countryOfManufacture

    # mengembalikan nilai atribut countryOfManufacture
    def getCountryOfManufacture(self):
        return self.__countryOfManufacture

    # menampilkan atribut Ship
    def printShip(self):
        print("type: " + self.getType())
        print("Fuel Type: " + self.getCountryOfManufacture())
