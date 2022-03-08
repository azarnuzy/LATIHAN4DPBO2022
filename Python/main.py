""" Saya Muhammad Azar Nuzy 2004191 mengerjakan Latihan 3 C1 dalam
mata kuliah DPBO untuk keberkahanNya maka saya tidak melakukan kecurangan
seperti yang telah dispesifikasikan. Aamiin """
# mengimport kelas
from lib2to3.pgen2 import driver
from turtle import pos
from Airplane import Airplane
from Ship import Ship
from Driver import Driver

# deklarasi variabel untuk masukan
name = ""
age = 0
countryOfManufacture = ""
fuelType = ""
typeShip = ""
maxPassangers = 0
wingsLength = 0
NIK = ""
gender = ""
NIP = ""
company = ""
position = ""
licenceId = ""

print("             Input Ship            ")
print("===================================")
# membuat instance array class dari Ship
ship = [Ship() for i in range(0, 5)]
print("-----------------------------------")
for i in range(0, 5):
    # masukan
    name = str(input("> Name: "))
    age = int(input("> Age: "))
    countryOfManufacture = str(input("> Country of Manufacture: "))
    fuelType = str(input("> Fuel Type: "))
    typeShip = str(input("> Type Ship: "))
    maxPassangers = int(input("> Max Passangers: "))
    print("-----------------------------------")
    # menetapkan nilai pada class ship
    ship[i].setName(name)
    ship[i].setAge(age)
    ship[i].setCountryOfManufacture(countryOfManufacture)
    ship[i].setFuelType(fuelType)
    ship[i].setType(typeShip)
    ship[i].setMaxPassengers(maxPassangers)

# membuat instance array class dari Airplane
print("          Input Airplane           ")
print("===================================")
airplane = [Airplane() for i in range(0, 5)]
print("-----------------------------------")
for i in range(0, 5):
    # masukan
    name = str(input("> Name: "))
    age = int(input("> Age: "))
    wingsLength = int(input("> Wings Length: "))
    fuelType = str(input("> Fuel Type: "))
    typeAirplane = str(input("> Type Airplane: "))
    maxPassangers = int(input("> Max Passangers: "))
    print("-----------------------------------")
    # menetapkan nilai pada class Airplane
    airplane[i].setName(name)
    airplane[i].setAge(age)
    airplane[i].setWingsLength(wingsLength)
    airplane[i].setFuelType(fuelType)
    airplane[i].setType(typeAirplane)
    airplane[i].setMaxPassengers(maxPassangers)


print("          Input Driver           ")
print("===================================")
driver = [Driver() for i in range(0, 5)]
print("-----------------------------------")
for i in range(0, 5):
    # masukan
    name = str(input("> Name: "))
    gender = str(input("> Gender: "))
    NIK = str(input("> NIK: "))
    NIP = str(input("> NIP: "))
    company = str(input("> Company: "))
    position = str(input("> Position: "))
    licenceId = str(input("> Licence Id: "))
    activeUntil = str(input("> Licence Id Active Until: "))
    vehicleType = str(input("> Vehicle Type: "))
    print("-----------------------------------")
    # menetapkan nilai pada class Driver
    driver[i].setName(name)
    driver[i].setNIK(NIK)
    driver[i].setGender(gender)
    driver[i].setNIP(NIP)
    driver[i].setCompanyName(company)
    driver[i].setPosition(position)
    driver[i].setLicenseId(licenceId)
    driver[i].setActiveUntil(activeUntil)
    driver[i].setVehicleType(vehicleType)

print("            Output Ship            ")
print("===================================")
print("-----------------------------------")
for i in range(0, 5):
    # masukan
    ship[i].printVehicle()
    ship[i].printShip()
    ship[i].move()
    print("-----------------------------------")

print("          Output Airplane          ")
print("===================================")
print("-----------------------------------")
for i in range(0, 5):
    # masukan
    airplane[i].printVehicle()
    airplane[i].printAirplane()
    airplane[i].move()
    print("-----------------------------------")


print("            Output Driver           ")
print("===================================")
print("-----------------------------------")
for i in range(0, 5):
    # masukan
    driver[i].printPerson()
    driver[i].printJob()
    driver[i].printDriver()
    driver[i].sleep()
    print("-----------------------------------")
