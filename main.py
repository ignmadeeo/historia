#imports
import time
import random
#info
def monster():
    return random.randint(1, 5)
monster1 = monster()
power = 2
staff = False
gold = 0
while True:
    name = input("vad heter du? ")
    if name.isdigit():
        print("svara med bokstäver!")
    else:
        break

age = input (f"Hur gammal är {name}? ")
print(f"den här historien handlar om {age}år gammla", name)
age = int(age) + 7
print("sju år senare var", name, age, "år gammal")
#story
choice = input("vill du gå till arenan? ja/nej? ")
if choice == "ja":
    if power >= monster1:
        print("Du vann mot svagt monster")
        gold = gold + 12
        power = power + 1
        print("du har", str(gold), "guld")
else:
    print("du går förbi en butik")
#shop
shop = input("vill du köpa något? ")
if shop == "ja":
    staff = input("vill du köpa den magiska staven för 10 guld ")
else:
    print("du går förbi butiken")
if staff == "ja":
    if gold >= 10:
        gold = gold - 10
        print("du har köpt staven")
        staff = True
if staff == True:
    power = power + 5
    print("din styrka ökade med 5")
    print("din styrka är nu", str(power))
walk = input("vill du gå på en promenad? ")
if walk == "ja":
    print("du börjar gå")
    time.sleep(3)
    print("din styrka är", str(power))
else:
    print("du går förbi")
    time.sleep(2)

#fortsättning på story

medium = input("du ser ett medium level monster vill du slåss mot monsteret? ")
if medium == "ja":
    if power >= 5:
        print("du vann")
else:
    print("du förlorade")
while True:
    if power >= 7:
        print("du har nått maximal styrka för din level")
        break
