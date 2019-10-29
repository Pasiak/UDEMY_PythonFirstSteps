import pickle
import glob


class Cake:
    known_kinds = ['cake', 'muffin', 'meringue', 'biscuit', 'eclair', 'christmas', 'pretzel', 'other']
    bakery_offer = []

    def __init__(self, name, kind, taste, additives, filling, gluten_free, text):

        self.name = name
        if kind in self.known_kinds:
            self.kind = kind
        else:
            self.kind = 'other'
        self.taste = taste
        self.additives = additives.copy()
        self.filling = filling
        self.bakery_offer.append(self)
        self.__gluten_free = gluten_free
        if self.kind == "cake" or text == "":
            self.__text = text
        else:
            print("Text has to be empty or kind needs to be 'cake'")

    def show_info(self):
        print("{}".format(self.name.upper()))
        print("Kind:        {}".format(self.kind))
        print("Taste:       {}".format(self.taste))
        if len(self.additives) > 0:
            print("Additives:")
            for a in self.additives:
                print("\t\t{}".format(a))
        if len(self.filling) > 0:
            print("Filling:     {}".format(self.filling))
        print("Gluten free: {}".format(self.__gluten_free))
        print('-' * 20)

    def set_filling(self, filling):
        self.filling = filling

    def add_additives(self, additives):
        self.additives.extend(additives)

    def __get_text(self):
        return self.__text

    def __set_text(self, newText):
        if self.kind == "cake":
            self.__text = newText
            print("done")
        else:
            print("New text can not be set")

    def save_to_file(self,path):
        with open(path, 'wb') as f:
            pickle.dump(self, f)

    @classmethod
    def read_from_file(cls, path):
        with open(path, 'rb') as f:
            new_cake = pickle.load(f)

        cls.bakery_offer.append(new_cake)
        return new_cake

    @staticmethod
    def get_bakery_files(dir):
        dir2 = dir + '/*.bakery'
        listoffiles =list(glob.glob(dir2))
        return listoffiles
    SetText = property(__get_text, __set_text, None, "Changing text")


cake01 = Cake('Vanilla Cake', 'cake', 'vanilla', ['chocolade', 'nuts'], 'cream', False, "Tekst")
cake02 = Cake('Chocolade Muffin', 'muffin', 'chocolade', ['chocolade'], '', False, "")
cake03 = Cake('Super Sweet Maringue', 'meringue', 'very sweet', [], '', True, "happy")
cake04 = Cake('Cocoa waffle', 'waffle', 'cocoa', [], 'cocoa', False, "100")

print("Today in our offer:")
for c in Cake.bakery_offer:
    c.show_info()

cake03.__gluten_free = False
print(dir(cake03))
cake03._Cake__gluten_free = False
cake03.show_info()
cake01.SetText = "Elo elo 320"

path = r"C:\Users\El Patrico\Desktop\tempTXT\BakeryLab.bakery"
dir =  r"C:\Users\El Patrico\Desktop\tempTXT"
cake01.save_to_file(path)
cake05 = Cake.read_from_file(path)

cake05.show_info()
print(Cake.get_bakery_files(dir))
