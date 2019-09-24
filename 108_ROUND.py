fsmaller = 3.14345435334534534
fbigger = 3.87754534543534534

import math

print(fsmaller, fbigger)
print("\n")

print (round(fsmaller,2),round(fbigger,2),round(fbigger,3))
print(min(fsmaller,fbigger), max(fsmaller,fbigger))

print("\n")

print(pow(2,8))    #potęgowanie
print(pow(9,0.5)) #pierwiastek z 9 = 3  | bo 9 do 1/2 = 3
print(math.sqrt(16)) #pierwiastek kwadratowy z 16


degree = 360
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
 
degree = 45
radian = degree * math.pi /180
print("%d degree is %f radians" % (degree, radian))
print('')
print("%d degree is %f radians" % (360, math.radians(360)))
print("%d degree is %f radians" % (45, math.radians(45)))
print('')

small_pizza_r = 22
big_pizza_r = 27
family_pizza_r = 38

small_pizza_price = 11.5
big_pizza_price = 16.6
family_pizza_price= 22

small_pizza_field = math.pi * pow(small_pizza_r,2)
print(small_pizza_field)
print(small_pizza_price/small_pizza_field)
print("")
print("")

big_pizza_field = math.pi * pow(big_pizza_r,2)
print(big_pizza_field)
print(big_pizza_price/big_pizza_field)
print("")
print("")

family_pizza_field = math.pi * pow(family_pizza_r,2)
print(family_pizza_field)
print(family_pizza_price/family_pizza_field)


math_ls = dir(math) 
print(math_ls)















#LAB
##
##percent = [2.606255012,1.222935044,1.283079391,3.628708901,6.856455493,4.911788292,
##           2.886928629,0.781876504,0.962309543,2.265437049,6.816359262,3.688853248,
##           3.468323978,5.633520449,4.530874098,1.984763432,0.922213312,3.327987169,
##           4.190056135,5.493183641,1.864474739,10.60545309,2.425821973,2.726543705,
##           8.740978348,6.174819567]
## 
##countries = ['Ukraine', 'Spain', 'Slovenia', 'Lithuania', 'Austria', 'Estonia',
##             'Norway', 'Portugal','United Kingdom','Serbia','Germany','Albania',
##             'France','Czech Republic','Denmark','Australia','Finland','Bulgaria',
##             'Moldova','Sweden','Hungary','Israel','Netherlands','Ireland',
##             'Cyprus','Italy']
##
##sumOfPoints = 4988
##print("------------------------")
##print("")
##print("")
##
##
##print(max(percent), "       ",min(percent))
##i=0
##for i in range(len(countries)-1):
##    print(countries[i])
##    print("------------------------")
##    print(percent[i])
##    print(int(percent[i]))
##    print(round(percent[i],2))
##    points = (sumOfPoints * percent[i])/100
##    print(points)
##
##    print("")
##    print(percent[i], int(percent[i]), round(percent[i],2), int(round(percent[i]*sumOfPoints/100,0)), countries[i])
## 
##    print("")
