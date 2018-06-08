from actions import *
import time

# Profession selection
print("Name: {}, HP: {}, AC: {}, EXP: {}, ATK: {}\n".format(
    hero.name, hero.hp, hero.ac, hero.EXP, hero.thaco))

# Mob encounter


print("You encountered " + mob.name + "!!! Defend Yourself", "", sep="\n")
time.sleep(1)
battle()


print("", "again", "You encountered " + mob.name + "!!! Defend Yourself", "", sep="\n")
time.sleep(1)
battle()


print("", "And again", "You encountered " + mob.name + "!!! Defend Yourself", "", sep="\n")
time.sleep(1)
battle()


print("", "And last time", "You encountered " + mob.name + "!!! Defend Yourself", "", sep="\n")
time.sleep(1)
battle()
