# kelas yang digunakan untuk mengimplementasikan Person
# kelas Person
class Person:
    # private atribute dari kelas Person
    __name = ""
    __NIK = ""
    __gender = ""

    def __init__(self, name="", NIK="", gender=""):
        # konstruktor
        self.__name = name
        self.__NIK = NIK
        self.__gender = gender

    # mengeset nilai atribut name
    def setName(self, name):
        self.__name = name

    # mengembalikan nilai atribut name
    def getName(self):
        return self.__name

    # mengeset nilai atribut NIK
    def setNIK(self, NIK):
        self.__NIK = NIK

    # mengembalikan nilai atribut NIK
    def getNIK(self):
        return self.__NIK

    # mengeset nilai atribut gender
    def setGender(self, gender):
        self.__gender = gender

    # mengembalikan nilai atribut gender
    def getGender(self):
        return self.__gender

    def sleep(self):
        print("This " + self.getName() + "is sleeping")

    # menampilkan atribut Person
    def printPerson(self):
        print("Name: " + self.getName())
        print("NIK: " + self.getNIK())
        print("Gender: " + self.getGender())
