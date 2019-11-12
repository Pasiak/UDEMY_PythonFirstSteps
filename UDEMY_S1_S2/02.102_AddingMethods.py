import csv
import types


def exportToFile_Static(path, header, data):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(header)
        writer.writerow(data)
    print("Function exportToFile - static")


def exportToFile_Class(cls, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Brand', 'Model', 'IsOnSale'])
        for c in cls.listOfCars:
            writer.writerow([c.brand, c.model, c.IsOnSale])

    print("Function exportToFile - class method")


def exportToFile_Instance(self, path):
    with open(path, mode="w") as file:
        writer = csv.writer(file, delimiter=' ', quotechar=',', quoting=csv.QUOTE_MINIMAL)
        writer.writerow(['Brand', 'Model', 'IsOnSale'])
        writer.writerow([self.brand, self.model, self.IsOnSale])

    print("Function exportToFile - instance method")


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

    IsOnSale = property(GetIsOnSale, SetIsOnSale, None, "Documentation")

    @classmethod
    def ReadFromText(cls, aText):
        aNewCar = cls(*aText.split(':'))
        return aNewCar

    @staticmethod
    def Convert_KM_KW(KM):
        return KM * 0, 735

    @staticmethod
    def Convert_KW_KM(KW):
        return KW * 0, 735


car_01 = Car("Opel", "Corsa", False, True, False)
car_02 = Car("skoda", "Fabia", False, True, True)

print("Static-------------" * 10)
exportToFile_Static(r"C:\Users\El Patrico\Desktop\tempTXT\02.102_Static.csv",
                    ['Brand', 'Model', 'IsOnSale'],
                    [car_01.brand, car_01.model, car_01.IsOnSale])

Car.ExportToFile_Class = types.MethodType(exportToFile_Class, Car)
Car.ExportToFile_Class(path=r"C:\Users\El Patrico\Desktop\tempTXT\02.102_Class.csv")
car_01.ExportToFile_Instance = types.MethodType(exportToFile_Instance, car_01)
car_01.ExportToFile_Instance(path=r"C:\Users\El Patrico\Desktop\tempTXT\02.102_Instance.csv")
