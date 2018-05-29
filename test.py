from actions import *
from monsters import *
import time

# Profession selection
print("Name: {}, HP: {}, AC: {}, EXP: {}, ATK: {}\n".format(
      hero.name, hero.hp, hero.ac, hero.EXP, hero.thaco))


# Mob encounter

print("You encountered " + mob.name + "!!! Defend Yourself", "", sep="\n")


# Fight mob
encounter()
print("", "again", "", sep="\n")
time.sleep(1)

encounter()
print("", "And again", "",  sep="\n")
time.sleep(1)

encounter()
print("", "And last time", "", sep="\n")
time.sleep(1)

encounter()
