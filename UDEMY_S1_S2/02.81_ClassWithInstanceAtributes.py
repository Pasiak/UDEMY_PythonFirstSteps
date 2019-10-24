class Car:
    numOfCars = 0
    listOfCars = []

    def __init__(self, brand, model, isAirbagOK):
        self.brand = brand
        self.model = model
        self.isAirbagOK = isAirbagOK
        Car.numOfCars +=1
        Car.listOfCars.append(self)

    def IsDamaged(self):
        return not self.isAirbagOK

    def GetInfo(self):
        print("*" * 30)
        print('Brand \t{}\nModel \t{}\nAirbags status\t{}\n'.format(self.brand, self.model, self.isAirbagOK))


car_01 = Car("Opel", "Corsa", False)

print(car_01.isAirbagOK, car_01.model, car_01.brand)
car_01.GetInfo()

print(Car.numOfCars)


# LAB

class Cake:

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        self.kind = kind
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling

    def ShowInfo(self):
        print("Name = {}".format(self.name).upper())
        print("Taste = {}".format(self.name))
        if self.additives:
            for a in self.additives:
                print("Addivites = {}".format(a))
        else:
            print("No Additives")

    def SetFilling(self, fillingName):
        self.filling = fillingName

    def SetAdditvites(self, add):
        self.additives.extend(add)


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream')
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '')
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '')

bakery_offer = []
bakery_offer.append(cake01)
bakery_offer.append(cake02)
bakery_offer.append(cake03)
cake03.SetFilling("NIC")
addivites = ["Cream", "Skittels", "MM"]
cake03.SetAdditvites(addivites)
print("Today in our offer:")

for c in bakery_offer:
    Cake.ShowInfo(c)
    print("*" * 30)


