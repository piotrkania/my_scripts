#!/usr/bin/python3

import random
from dice import *
from professions import *
from monsters import *
import time

def PlayerAttack():
    roll=twenty_sided_die.roll()
    if roll >= hero.thaco - mob.ac:
        rollD = random.choice(hero.POWER)
        print(hero.name + " rolled " + str(roll) + " and  hit " + mob.name + " for " + str(rollD) + " damage.")
        print("")
        mob.hp -= rollD
        print(mob.name + " has " + str(mob.hp) + " hp left.")
        print("")
    else:
        print(hero.name + " rolled " + str(roll) + " and missed.")
        print("")


def MonsterAttack():
    roll=twenty_sided_die.roll()
    if roll >= mob.thaco - hero.ac:
        rollD = random.choice(mob.POWER)
        print(mob.name + " rolled " + str(roll) + " and hits You for " + str(rollD) + " damage." )
        print("")
        hero.hp -= rollD
        print(hero.name + " has " + str(hero.hp) + " hp left.")
        print("")
    else:
        print(mob.name + " rolled " + str(roll) + " and missed.")
        print("")

def Level_Up():
    hero.LEVEL += 1
    hero.LVL_EXP = hero.LVL_EXP*2
    hp_gain = level_up_die.roll()
    hero.MAX_HP += hp_gain
    print("LEVEL UP!!! Gained " + str(hp_gain) + "HP.")
    print("")
    hero.hp = hero.MAX_HP
    print("Name: {}, HP: {}, EXP: {}, LEVEL: {} \n".format(
           hero.name, hero.hp, hero.EXP, hero.LEVEL))

def encounter():
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
                    break
                    time.sleep(1)
                else:
                    continue
            elif mob.hp <= 0 and hero.hp > 0 :
                print("++++++You killed " + mob.name+ "++++++")
                print("")
                print("Gained " + str(mob.exp) + " XP.")
                print("")
                hero.EXP += mob.exp
                if hero.EXP >= hero.LVL_EXP:
                    Level_Up()
                    break
                break
                time.sleep(1)
            exit(0)
