#!/usr/bin/python3

import welcome
from professions import *
from dice import *
from actions import *
from monsters import *
import time
import races
import spells

# Profession selection

print("Name: {}, HP: {}, AC: {}, EXP: {}, ATK: {}\n".format(
      hero.name, hero.hp, hero.ac, hero.exp, hero.thaco))


# Enter the building
for command, action in hero.COMMANDS.items():
    print("Press {} to {}".format(command, action[0]))

while True:
    command = input("~~~~~~~Press key to continue~~~~~~~")
    if command not in hero.COMMANDS:
        print("Not a valid command")
        continue
    print("You are fighting "  + mob.name)
    print("")
    time.sleep(1)
    break

while True:
    if command:
        hero.COMMANDS[command][1]()
        PlayerAttack()
        time.sleep(1)
        if mob.hp > 0:
            MonsterAttack()
            time.sleep(1)
            if hero.hp <= 0:
                print("++++++You were killed++++++")
                time.sleep(1)
                break
            else:
                continue
        elif mob.hp <= 0 and hero.hp > 0 :
            print("++++++You killed " + mob.name+ "++++++")
            print("")
            print("Gained " + str(mob.exp) + " XP.")
            time.sleep(1)
            break
    Level_Up()

# Encounter command
