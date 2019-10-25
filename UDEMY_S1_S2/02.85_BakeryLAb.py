# LAB

class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling):
        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)

    def ShowInfo(self):
        print("Name = {}".format(self.name).upper())
        print("Kind = {}".format(self.kind))
        print("Taste = {}".format(self.taste))
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
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa')

cake03.SetFilling("NIC")
addivites = ["Cream", "Skittels", "MM"]
cake03.SetAdditvites(addivites)
print("Today in our offer:")

for c in Cake.bakery_offer:
    Cake.ShowInfo(c)
    print("*" * 30)

print(isinstance(car_01, Cake))
print("Vars", vars(cake01))
print("Vars", vars(Cake))
print("dir", dir(cake01))
print("dir", dir(Cake))
