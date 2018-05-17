#!/usr/bin/python3

class Item:
   def __init__(self,name):
       self.name = name

class HP_potion(Item):
    def __init__(self):
        super().__init__(name = "HP Potion")

    HP = 3

class MP_potion(Item):
    def __init__(self):
        super().__init__(name = "MP Potion")

    MP = 3

class Sword(Item):
    def __init__(self):
        super().__init__(name = "Sword")

    ATK = 1

def equipment():
    equipment = ["Sword", "MP Potion", "HP Potion"]
    while True:
        for item in equipment:
            return item


item = equipment()
