# Import kelas Person dan Job
from Person import Person
from Job import Job


# kelas yang digunakan untuk mengimplementasikan Driver
# kelas Driver
class Driver(Person, Job):
    # private atribute dari kelas Driver
    __licenseId = ""
    __activeUntil = ""
    __vehicleType = ""

    def __init__(self, licenseId="", activeUntil="", vehicleType=""):
        # konstruktor
        self.__licenseId = licenseId
        self.__activeUntil = activeUntil
        self.__vehicleType = vehicleType

    # mengeset nilai atribut licenseId
    def setLicenseId(self, licenseId):
        self.__licenseId = licenseId

    # mengembalikan nilai atribut licenseId
    def getLicenseId(self):
        return self.__licenseId

    # mengeset nilai atribut activeUntil
    def setActiveUntil(self, activeUntil):
        self.__activeUntil = activeUntil

    # mengembalikan nilai atribut activeUntil
    def getActiveUntil(self):
        return self.__activeUntil

    # mengeset nilai atribut vehicleType
    def setVehicleType(self, vehicleType):
        self.__vehicleType = vehicleType

    # mengembalikan nilai atribut vehicleType
    def getVehicleType(self):
        return self.__vehicleType

    # menampilkan atribut Driver
    def printDriver(self):
        print("License Id: " + self.getLicenseId())
        print("Active Until: " + self.getActiveUntil())
        print("Vehicle Type: " + self.getVehicleType())
