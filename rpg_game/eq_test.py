from professions import *


def equip():
    for item in hero.INVENTORY:
        if item.type == "weapon":
            print(item)


equip()
