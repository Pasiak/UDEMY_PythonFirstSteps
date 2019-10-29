brandOnSale = "Opel"

class Car:
    numOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirbagOK, isTaxi, isOnSale):
        self.brand = brand
        self.model = model
        self.isAirbagOK = isAirbagOK
        self.__isTaxi = isTaxi
        self.__isOnSale = isOnSale
        Car.numOfCars += 1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not self.isAirbagOK

    def GetInfo(self):
        print("*" * 30)
        print('Brand \t{}\nModel \t{}\nAirbags status\t{}\nIs Taxi {}\t'.format(self.brand, self.model, self.isAirbagOK,
                                                                                self.__isTaxi))

    def GetIsOnSale(self):
        return self.__isOnSale

    def SetIsOnSale(self, newIsOnSaleStatus):
        if self.brand == brandOnSale:
            self.__isOnSale = newIsOnSaleStatus
            print('Changing IsOnSale stratus to {} for {}'.format(newIsOnSaleStatus, self.brand))
        else:
            print("Can not change IsONsale status. Sale valid only for {}".format(brandOnSale))

    IsOnSale = property(GetIsOnSale, SetIsOnSale, None,"Documentation" )

    @classmethod
    def ReadFromText(cls,aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0,735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW * 0, 735

car_01 = Car("Opel", "Corsa", False, True, False)
car_02 = Car("skoda", "Fabia", False, True, True)

print("Cars status:", car_01.GetIsOnSale(), car_02.GetIsOnSale())
car_01.SetIsOnSale(True)
car_02.SetIsOnSale(True)
car_01.IsOnSale = True
car_02.IsOnSale = True

lineOfText = "Renault:Megane:True:True:False"
car_04 = Car.ReadFromText(lineOfText)
print(car_04.GetInfo())