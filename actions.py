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

def Level_Up():
    while hero.exp >= hero.LEVEL_2:
        levelGain = False
        hero.LEVEL += 1
        levelGain = True
        hero.LEVEL_2 = hero.LEVEL_2*2
        if levelGain == True:
            hp_gain = level_up_die.roll()
            hero.MAX_HP += hp_gain
            print("LEVEL UP!!! Gained " + str(hp_gain) + "HP.")
            print("")
            hero.hp = hero.MAX_HP
            print("Name: {}, HP: {}, LEVEL: {}\n".format(
                  hero.name, hero.hp, hero.LEVEL))
