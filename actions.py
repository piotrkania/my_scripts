#!/usr/bin/python3

from dice import *
from professions import *
from monsters import *

def PlayerAttack():
    roll=twenty_sided_die.roll()
    if roll >= hero.thaco - mob.ac:
        rollD = hero.MAX_POWER
        print(hero.name + " rolled " + str(roll) + " and  hit " + mob.name + " for " + str(rollD) + " damage.")
        print("")
        mob.hp -= rollD
        print(mob.name + " has " + str(mob.hp) + " hp left.")
        print("")
    else:
        print(hero.name + " rolled " + str(roll) + " and missed.")
        print("")


def MonsterAttack():
    roll=ten_sided_die.roll()
    if roll >= mob.thaco-hero.ac:
        rollD = mob.MAX_POWER
        print(mob.name + " rolled " + str(roll) + " and hits You for " + str(rollD) + "." )
        print("")
        hero.hp -= rollD
        print(hero.name + " has " + str(hero.hp) + " hp left.")
        print("")
    else:
        print(mob.name + " rolled " + str(roll) + " and missed.")
        print("")

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
