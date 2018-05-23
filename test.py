#!/usr/bin/python3

import welcome
from professions import *
from dice import *
from actions import *
from monsters import *
import time

# Profession selection
print("Name: {}, HP: {}, AC: {}, EXP: {}, ATK: {}\n".format(
      hero.name, hero.hp, hero.ac, hero.EXP, hero.thaco))


# Mob encounter

print("You encountered a monster!!! Defend Yourself")


# Fight mob
encounter()

print("", "again", "", sep="\n")

encounter()


print("", "And again", "",  sep="\n")

encounter()


print("", "And last time", "", sep="\n")

encounter()
