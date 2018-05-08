#!/usr/bin/python3

import random
from dice import *
from professions import *
from monsters import *
from spells import *
import time

def PlayerAttack():
    roll = twenty_sided_die.roll()
    if roll >= hero.thaco - mob.ac :
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
    roll = twenty_sided_die.roll()
    if roll >= mob.thaco - hero.ac :
        rollD = random.choice(mob.POWER)
        print(mob.name + " rolled " + str(roll) + " and hits You for " + str(rollD) + " damage." )
        print("")
        hero.hp -= rollD
        print(hero.name + " has " + str(hero.hp) + " hp left.")
        print("")
    else:
        print(mob.name + " rolled " + str(roll) + " and missed.")
        print("")

def CastSpell():
    roll = four_sided_die.roll()
    if roll >= 2 :
        print(hero.name + " rolled " + str(roll) + " and successfuly concentrated to prepare a spell")
        print("")
        spell = choose_spell()
        spellD = random.choice(spell.DAMAGE)
        print("You cast " + spell.name + " and deal " + str(spellD) + " damage to " + mob.name)
        print("")
        hero.mana -= spell.MANA
        mob.hp -= spellD
        print(mob.name + " has " + str(mob.hp) + " hp left.")
    else:
        print(hero.name + " rolled " + str(roll) + " and failed to prepare a spell.")
        print("")


def Level_Up():
    hero.LEVEL += 1
    hero.LVL_EXP = hero.LVL_EXP*2
    if hero.PROF == "FIGHTER":
        hp_gain = level_up_die.roll()
        hero.MAX_HP += hp_gain
        print("LEVEL UP!!! Gained " + str(hp_gain) + "HP.")
        print("")
        hero.hp = hero.MAX_HP
        print("Name: {}, HP: {}, EXP: {}, LEVEL: {} \n".format(
              hero.name, hero.hp, hero.EXP, hero.LEVEL))
    elif hero.PROF == "MAGE":
        hp_gain = level_up_die.roll()
        mana_gain = level_up_die.roll()
        hero.MAX_HP += hp_gain
        hero.MAX_MANA += mana_gain
        print("LEVEL UP!!! Gained " + str(hp_gain) + " HP" + " and " + str(mana_gain) + " MP.")
        print("")
        hero.hp = hero.MAX_HP
        hero.mana = hero.MAX_MANA
        print("Name: {}, HP: {}, MP: {},  EXP: {}, LEVEL: {} \n".format(
              hero.name, hero.hp, hero.mana, hero.EXP, hero.LEVEL))


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
    while True :
        if command == "f":
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
            elif mob.hp <= 0 and hero.hp > 0:
                print("++++++You killed " + mob.name + "++++++")
                print("")
                print("Gained " + str(mob.exp) + "XP.")
                print("")
                hero.EXP += mob.exp
                mob.hp = mob.MAX_HP
                if hero.EXP >= hero.LVL_EXP:
                    Level_Up()
                    break
                break
                time.sleep(1)
            break
        elif command == "s":
            if hero.MANA >= 1:
                CastSpell()
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
                elif mob.hp <= 0 and hero.hp > 0:
                    print("++++++You killed " + mob.name + "++++++")
                    print("")
                    print("Gained " + str(mob.exp) + "XP.")
                    print("")
                    hero.EXP += mob.exp
                    hero.mana = hero.MAX_MANA
                    mob.hp = mob.MAX_HP
                    if hero.EXP >= hero.LVL_EXP:
                        Level_Up()
                        break
                    break
                    time.sleep(1)
            elif hero.MANA < 1:
                print("Not enough mana")
                continue
            break
