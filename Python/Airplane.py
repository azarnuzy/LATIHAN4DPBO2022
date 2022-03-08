# Import kelas Vehicle
from Vehicle import Vehicle

# kelas yang digunakan untuk mengimplementasikan Airplane
# kelas Airplane


class Airplane:
    # private atribute dari kelas Airplane
    __type = ""
    __wingsLength = 0

    def __init__(self, type="", wingsLength=0):
        # konstruktor
        super().__init__()
        self.__type = type
        self.__wingsLength = wingsLength

    # mengeset nilai atribut type
    def setType(self, type):
        self.__type = type

    # mengembalikan nilai atribut type
    def getType(self):
        return self.__type

    # mengeset nilai atribut wingsLength
    def setWingsLength(self, wingsLength):
        self.__wingsLength = wingsLength

    # mengembalikan nilai atribut wingsLength
    def getWingsLength(self):
        return self.__wingsLength

    # menampilkan atribut Airplane
    def printAirplane(self):
        print("type      : " + self.getType())
        print("Wings Length : " + str(self.getWingsLength()))
