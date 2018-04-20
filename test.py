#!/usr/bin/python3

import welcome
from dice import *
from professions import *
from monsters import *
from actions import *
import races
import spells

# Profession selection

print("Name: {}, HP: {}, AC: {}, EXP: {}, ATK: {}\n".format(
      hero.name, hero.hp, hero.ac, hero.exp, hero.thaco))


# Enter the building

while True:
    start=input("Hit 'Enter' to enter the building: ")
    if start=="":
        print("You slowly enter the mansion")
        break
    else:
        print("Are You sure You dont't want to know whats behind the door ?")
        continue


for command, action in hero.COMMANDS.items():
    print("Press {} to {}".format(command, action[0]))

while True:
    command = input("~~~~~~~Press key to continue~~~~~~~")
    if command not in hero.COMMANDS:
        print("Not a valid command")
        continue
    break
print("You are fighting "  + mob.name)

while True:
    if command:
        hero.COMMANDS[command][1]()
        PlayerAttack()
        if mob.hp > 0:
            MonsterAttack()
            continue
        else:
            print("You killed " + mob.name)
            print("")
            print("Gained " + str(mob.exp) + "XP.")
            print("")
            Level_Up()
            break
