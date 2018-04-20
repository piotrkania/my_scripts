#!/usr/bin/python3

from random import randint
from professions import *

# Defines die roll

class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

# Die types

level_up_die = Die(hero.HD)
four_sided_die = Die(4)
six_sided_die = Die(6)
ten_sided_die = Die(10)
twenty_sided_die = Die(20)
