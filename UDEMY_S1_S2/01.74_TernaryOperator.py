#!/usr/bin/env python
# coding: utf-8

itRains = True
if itRains:
    print("We stay at home")
else:
    print("We go out")

print("We stay at home" if itRains else "We go out")
#LAB

musclePain  = False
fever = False
weakness = True
isMan =True
print("suspicion of influenza" if musclePain and fever and weakness else "The flu is unlikely")

if musclePain and fever and weakness:
    print("suspicion of influenza")
elif weakness and (not fever or musclePain):
    print("Just take a rest!")
else:
    print("you may be cold")



