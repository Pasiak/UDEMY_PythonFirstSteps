car_01 = {
    'carBrand': 'Seat',
    'carModel': 'Ibiza',
    'carIsAirBagOK': True,
    'carIsPaintingOK': True,
    'carIsMachanicOK': True
}
car_02 = {
    'carBrand': 'Seat',
    'carModel': 'Toledo',
    'carIsAirBagOK': False,
    'carIsPaintingOK': True,
    'carIsMachanicOK': True
}

def IsCarDamaged(aCar):
    return  not (aCar['carIsAirBagOK'] and aCar['carIsMachanicOK'] and aCar['carIsPaintingOK'])

print(IsCarDamaged(car_01))
print(IsCarDamaged(car_02))

cars = [car_01,car_02]

for c in cars:
    print("{} {} damaged = {}".format(c['carBrand'],c['carModel'],IsCarDamaged(c)))

#LAB
cake_01 = {
    'taste' : 'vanilia',
    'glaze' : 'chocolade',
    'text' : 'Happy Brithday',
    'weight' : 0.7
}
cake_02 = {
    'taste' : 'tee',
    'glaze' : 'lemon',
    'text' : 'Happy Python Coding',
    'weight' : 1.3
}




def show_cake_info(cake):
    print('{} cake with {} glaze with text "{}" of {} kg'.format(
        cake['taste'], cake['glaze'], cake['text'], cake['weight']))
    print('*' * 30)

cakes = [cake_01,cake_02]

for c in cakes:
    print(show_cake_info(c))
