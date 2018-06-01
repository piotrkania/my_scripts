from professions import *
from random import randint


# Defines die roll

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)


# Die types


four_sided_die = Die(4)
six_sided_die = Die(6)
ten_sided_die = Die(10)
twenty_sided_die = Die(20)
loot_die = Die(2)