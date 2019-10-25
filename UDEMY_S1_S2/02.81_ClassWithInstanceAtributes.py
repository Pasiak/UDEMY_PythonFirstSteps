class Car:
    numOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirbagOK, isTaxi):
        self.brand = brand
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.__isTaxi = isTaxi
        Car.numOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not self.isAirbagOK

    def GetInfo(self):
        print("*" * 30)
        print('Brand \t{}\nModel \t{}\nAirbags status\t{}\nIs Taxi {}\t'.format(self.brand, self.model, self.isAirbagOK,
                                                                                self.__isTaxi))


car_01 = Car("Opel", "Corsa", False, True)

print(car_01.isAirbagOK, car_01.model, car_01.brand)
car_01.GetInfo()
car_01.YearOfProduction = 2006
del  car_01.YearOfProduction

setattr(car_01,"KM",123532)
delattr(car_01,"KM")
print(hasattr(car_01,"brand"))
print("Vars:", vars(car_01))
print("Number of Cars ", Car.numOfCars)


