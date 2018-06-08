from dice import *
from professions import *
from monsters import *
import time
from spells import *
from potions import *
from weapons import *


def player_attack():
    """ This function defines how the player character attacks, depending on the roll of 20-sided Die """

    roll = twenty_sided_die.roll()
    if roll >= hero.thaco - mob.ac:
        rollD = random.choice(hero.ATK)
        print(hero.name + " rolled " + str(roll) + " and hit " + mob.name + " for " + str(rollD) + " damage.", "",
              sep="\n")
        mob.hp -= rollD
        print(mob.name + " has " + str(mob.hp) + " hp left.", "", sep="\n")
    else:
        print(hero.name + " rolled " + str(roll) + " and missed.", "", sep="\n")


def monster_attack():
    """ This function defines how the monster character attacks,  depending on the roll of 20-sided Die """

    roll = twenty_sided_die.roll()
    if roll >= mob.thaco - hero.ac:
        rollD = random.choice(mob.ATK)
        print(mob.name + " rolled " + str(roll) + " and hits You for " + str(rollD) + " damage.", "", sep="\n")
        hero.hp -= rollD
        print(hero.name + " has " + str(hero.hp) + " hp left.", "", sep="\n")
    else:
        print(mob.name + " rolled " + str(roll) + " and missed.", "", sep="\n")


def cast_spell():
    """ This function defines how the Player character cast spells. There is 50/50 chance that Player will
        fail/succeed preparing a spell """

    roll = four_sided_die.roll()
    if roll >= 2:
        print(hero.name + " rolled " + str(roll) + " and successfully concentrated to prepare a spell", "",
              sep="\n")
        spell = choose_spell()
        while True:
            if hero.mana >= spell.MANA:
                spellD = random.choice(spell.DAMAGE)
                print("You cast " + spell.name + " and deal " + str(spellD) + " damage to " + mob.name, "",
                      sep="\n")
                hero.mana -= spell.MANA
                mob.hp -= spellD
                print(mob.name + " has " + str(mob.hp) + " hp left.", "", sep="\n")
                print("You have " + str(hero.mana) + " mana left.", "", sep="\n")
                break
            else:
                print("", "Not enough mana...", "", sep="\n")
                break
    else:
        print(hero.name + " rolled " + str(roll) + " and failed to prepare a spell.", "", sep="\n")


def level_up():
    """ This function defines how and when player characters gains experience and level up """

    hero.LEVEL += 1
    hero.LVL_EXP = hero.LVL_EXP * 2
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


def equipment():
    eq = [HpPotion(), MpPotion(), ShortSword(), LongSword(), BastardSword()]
    while True:
        for i in eq:
            return i


item = equipment()


def loot():
    """ This functions defines how player character gathers loot after defeating an enemy(mob). """
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
    """ This function defines player character encounter with a random monster, depending of the chosen command,
    player / monster takes appropriate action """

    while True:
        for command, action in hero.COMMANDS.items():
            print("Press {} to {}".format(command, action[0]))
        command = input("~~~~~~~Press key to continue~~~~~~~")
        if command not in hero.COMMANDS:
            print("Not a valid command")
            continue
        else:
            if command == "i":
                print(hero.INVENTORY)
                continue
            elif command == "h":
                potion = 'HP Potion'
                if potion in hero.INVENTORY:
                    hero.hp += item.HP
                    hero.INVENTORY.remove(potion)
                    print("You healed for " + str(item.HP) + "HP", "", sep="\n")
                    continue
                else:
                    print("You have no healing potion in your inventory", "", sep="\n")
                    continue
            elif command == "m":
                potion = 'MP'
                if potion in hero.INVENTORY:
                    hero.mana += item.MP
                    hero.INVENTORY.remove(potion)
                    print("You restored " + str(item.MP) + " mana points.", "", sep="\n")
                    continue
                else:
                    print("You have no mana potion in your inventory", "", sep="\n")
                    continue
            elif command == "f":
                hero.fight()
            elif command == "s":
                cast_spell()
                time.sleep(1)
                if mob.hp > 0:
                    monster_attack()
                    time.sleep(1)
                    if hero.hp <= 0:
                        print("++++++You were killed++++++")
                        break
                    else:
                        continue
                else:
                    print("++++++You killed " + mob.name + "++++++", "", sep="\n")
                    print("Gained " + str(mob.exp) + "XP.", "", sep="\n")
                    loot()
                    hero.EXP += mob.exp
                    mob.hp = mob.MAX_HP
                    if hero.EXP >= hero.LVL_EXP:
                        level_up()
                        break
                    else:
                        hero.hp = hero.MAX_HP
                    time.sleep(1)
                    break
            break


encounter()