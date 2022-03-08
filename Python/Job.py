# kelas yang digunakan untuk mengimplementasikan Job
# kelas Job
class Job:
    # private atribute dari kelas Job
    __companyName = ""
    __NIP = ""
    __position = ""

    def __init__(self, companyName="", NIP="", position=""):
        # konstruktor
        self.__companyName = companyName
        self.__NIP = NIP
        self.__position = position

    # mengeset nilai atribut companyName
    def setCompanyName(self, companyName):
        self.__companyName = companyName

    # mengembalikan nilai atribut companyName
    def getCompanyName(self):
        return self.__companyName

    # mengeset nilai atribut NIP
    def setNIP(self, NIP):
        self.__NIP = NIP

    # mengembalikan nilai atribut NIP
    def getNIP(self):
        return self.__NIP

    # mengeset nilai atribut position
    def setPosition(self, position):
        self.__position = position

    # mengembalikan nilai atribut position
    def getPosition(self):
        return self.__position

    # menampilkan atribut Job
    def printJob(self):
        print("Company Name: " + self.getCompanyName())
        print("NIP: " + self.getNIP())
        print("Position: " + self.getPosition())
