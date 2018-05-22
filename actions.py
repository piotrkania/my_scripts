#!/usr/bin/python3

import random
from dice import *
from professions import *
from monsters import *
from spells import *
import time


def PlayerAttack():
    """ This function defines how the player character attacks """
    
    roll = twenty_sided_die.roll()
    if roll >= hero.thaco - mob.ac :
        rollD = random.choice(hero.POWER)
        print(hero.name + " rolled " + str(roll) + " and hit " + mob.name + " for " + str(rollD) + " damage.", "", sep="\n")
        mob.hp -= rollD
        print(mob.name + " has " + str(mob.hp) + " hp left.", "", sep="\n")
    else:
        print(hero.name + " rolled " + str(roll) + " and missed.", "", sep="\n")


def MonsterAttack():
    """ This function defines how the monster character attacks """
    
    roll = twenty_sided_die.roll()
    if roll >= mob.thaco - hero.ac :
        rollD = random.choice(mob.POWER)
        print(mob.name + " rolled " + str(roll) + " and hits You for " + str(rollD) + " damage.", "", sep="\n")
        hero.hp -= rollD
        print(hero.name + " has " + str(hero.hp) + " hp left.", "",  sep="\n")
    else:
        print(mob.name + " rolled " + str(roll) + " and missed.", "", sep="\n")


def CastSpell():
    """ This function defines how the spells are being generated and casted by player character """
    
    roll = four_sided_die.roll()
    while True:
        if hero.mana >= 1:
            if roll >= 2 :
                print(hero.name + " rolled " + str(roll) + " and successfuly concentrated to prepare a spell", "", sep="\n")
                spell = choose_spell()
                if hero.mana < spell.MANA:
                    print("", "Not enough mana...", "", sep="\n")
                    continue
                else:
                    spellD = random.choice(spell.DAMAGE)
                    print("You cast " + spell.name + " and deal " + str(spellD) + " damage to " + mob.name, "", sep="\n")
                    hero.mana -= spell.MANA
                    mob.hp -= spellD
                    print(mob.name + " has " + str(mob.hp) + " hp left.", "", sep="\n")
                    print("You have " + str(hero.mana) + " mana left.", "", sep="\n")
                    break
            else:
                print(hero.name + " rolled " + str(roll) + " and failed to prepare a spell.", "", sep="\n")
                break
        else:
            continue


def Level_Up():
    """ This function defines how and when player charcters gains experience and level up """
    
    hero.LEVEL += 1
    hero.LVL_EXP = hero.LVL_EXP*2
    if hero.PROF == "FIGHTER":
        hp_gain = level_up_die.roll()
        hero.MAX_HP += hp_gain
        print("LEVEL UP!!! Gained " + str(hp_gain) + "HP." "", sep="\n")
        hero.hp = hero.MAX_HP
        print("Name: {}, HP: {}, MP: {}, EXP: {}, LEVEL: {} \n".format(
              hero.name, hero.hp, hero.mana, hero.EXP, hero.LEVEL))
    elif hero.PROF == "MAGE":
        hp_gain = level_up_die.roll()
        mana_gain = level_up_die.roll()
        hero.MAX_HP += hp_gain
        hero.MAX_MANA += mana_gain
        print("LEVEL UP!!! Gained " + str(hp_gain) + " HP" + " and " + str(mana_gain) + " MP.", "", sep="\n")
        hero.hp = hero.MAX_HP
        hero.mana = hero.MAX_MANA
        print("Name: {}, HP: {}, MP: {},  EXP: {}, LEVEL: {} \n".format(
              hero.name, hero.hp, hero.mana, hero.EXP, hero.LEVEL))

def loot():
    """ This functions defines how player character gathers loot """
    
    while True:
        rollL = loot_die.roll()
        if rollL == 1:
            loot_item = random.choice(mob.INVENTORY)
            hero.INVENTORY.append(loot_item)
            print("You search the corpse and found " + str(loot_item))
            break
        else:
            print("You search the corpse but found nothing", "", sep="\n")
            break


def encounter():
    
 """ This function defines player character encounter with a random monster, dpeneding of the choosen command,
 player / monster takes appropriate action """
 
    for command, action in hero.COMMANDS.items():
        print("Press {} to {}".format(command, action[0]))
    while True:
        command = input("~~~~~~~Press key to continue~~~~~~~")
        if command not in hero.COMMANDS:
            print("Not a valid command")
            continue
        elif command == "i":
            print(hero.INVENTORY)
            continue
        elif command == "h":
            potion = 'Hg'
            if potion in hero.INVENTORY:
                hero.hp += item.HP
                print("You healed for " + str(item.HP) + "HP", "", sep="\n")
                continue
            else:
                print("You have no potion in your inventory", "", sep="\n")
            continue
        elif command == "m":
            potion = 'Mana'
            if potion in hero.INVENTORY:
                hero.mana += item.MP
                print("You restored " + str(item.MP) + " mana points.", "", sep="\n")
        print("You are fighting "  + mob.name, "", sep="\n")
        time.sleep(1)
        break
    while True :
        if command == "f":
            time.sleep(1)
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
                print("++++++You killed " + mob.name + "++++++", "", sep="\n")
                print("Gained " + str(mob.exp) + "XP.", "", sep="\n")
                loot()
                hero.EXP += mob.exp
                mob.hp = mob.MAX_HP
                if hero.EXP >= hero.LVL_EXP:
                    Level_Up()
                    break
                else:
                    hero.hp = hero.MAX_HP
                time.sleep(1)
            break
        elif command == "s":
            if hero.mana >= 1:
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
                    print("++++++You killed " + mob.name + "++++++", "", sep="\n")
                    print("Gained " + str(mob.exp) + "XP.", "", sep="\n")
                    loot()
                    hero.EXP += mob.exp
                    hero.mana = hero.MAX_MANA
                    mob.hp = mob.MAX_HP
                    if hero.EXP >= hero.LVL_EXP:
                        Level_Up()
                        break
                    break
                    time.sleep(1)
            elif hero.mana < 1:
                print("Not enough mana", "", sep="\n")
                print("Melee attack", "", sep="\n")
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
                    print("++++++You killed " + mob.name + "++++++", "", sep="\n")
                    print("Gained " + str(mob.exp) + "XP.", "", sep="\n")
                    hero.EXP += mob.exp
                    mob.hp = mob.MAX_HP
                    if hero.EXP >= hero.LVL_EXP:
                        Level_Up()
                        break
                    break
                    time.sleep(1)
                break
            break
