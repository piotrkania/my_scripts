from dice import *
from weapons import *
from monsters import *
from potions import *
import time
from spells import *


class Player:

    EQUIPMENT_SLOTS = {'Head': None, 'Chest': None, 'Bracers': None, "Belt": None, "Legs": None, 'Boots': None,
                       'Necklace': None, 'Left ring': None, 'Right ring': None, 'Hand': None, 'Off-hand': None}

    def __init__(self, name, hp, ac, mana):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.mana = mana
        self.thaco = 20

    @staticmethod
    def check_equipment():
        """ This method prints items currently equipped in each slot"""

        slots = hero.EQUIPMENT_SLOTS
        for k, v in slots.items():
            print('%s: %s' % (k, v))

    @staticmethod
    def heal():
        """ This method defines how hit points (HP) points are being restored. If restored HPs exceeds Players
        MAX_HP, players HP will be set to MAX_HP"""

        while heal_pot in hero.INVENTORY:
            hero.hp += heal_pot.HP
            print("", "You healed for " + str(heal_pot.HP) + "HP", "", sep="\n")
            hero.INVENTORY.remove(heal_pot)
            if hero.hp > hero.MAX_HP:
                hero.hp = hero.MAX_HP
            break
        else:
            print("", "You have no healing potion in your inventory", "", sep="\n")

    @staticmethod
    def refresh_mana():
        """ This method defines how mana points are being restored"""

        while mana_pot in hero.INVENTORY:
            hero.mana += mana_pot.MP
            print("", "You restored " + str(mana_pot.MP) + "MP", "", sep="\n")
            hero.INVENTORY.remove(mana_pot)
            if hero.mana > hero.MAX_MANA:
                hero.mana = hero.MAX_MANA
            break
        else:
            print("", "You have no mana potion in your inventory", "", sep="\n")

    def inventory(self):
        """ This method prints Players inventory """

        if not hero.INVENTORY:
            print("\n", "Inventory is empty", "\n")
        else:
            for it in hero.INVENTORY:
                print(it.__str__())

    @staticmethod
    def equip():

        n = 0
        while True:
            for k in slot.keys():
                n += 1
                print("Press {} to equip {}".format(n, '%s' % k))
            option = input("Choose slot You wish to equip >>>>> ")
            if option == "10":
                from equip_item import equip_hand
                equip_hand()
            else:
                print("Choose the correct slot")
                continue

    @staticmethod
    def player_attack():
        """ This method defines how the player character attacks, depending on the roll of 20-sided Die """

        roll = twenty_sided_die.roll()
        if roll >= hero.thaco - mob.ac:
            rollD = hero.ATK
            print(hero.name + " rolled " + str(roll) + " and hit " + mob.name + " for " + str(rollD) + " damage.", "",
                  sep="\n")
            mob.hp -= rollD
            print(mob.name + " has " + str(mob.hp) + " hp left.", "", sep="\n")
        else:
            print(hero.name + " rolled " + str(roll) + " and missed.", "", sep="\n")

    @staticmethod
    def monster_attack():
        """ This method defines how the monster character attacks,  depending on the roll of 20-sided Die """

        roll = twenty_sided_die.roll()
        if roll >= mob.thaco - hero.ac:
            rollD = random.choice(mob.ATK)
            print(mob.name + " rolled " + str(roll) + " and hits You for " + str(rollD) + " damage.", "", sep="\n")
            hero.hp -= rollD
            print(hero.name + " has " + str(hero.hp) + " hp left.", "", sep="\n")
        else:
            print(mob.name + " rolled " + str(roll) + " and missed.", "", sep="\n")

    @staticmethod
    def level_up():
        """ This method defines how and when player characters gains experience and level up """

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

    @staticmethod
    def loot():
        """ This method defines how player character gathers loot after defeating an enemy(mob). """

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

    @staticmethod
    def fight():
        """ This method defines how the melee fight is being performed """

        while True:
            time.sleep(1)
            hero.player_attack()
            time.sleep(1)
            if mob.hp > 0:
                hero.monster_attack()
                time.sleep(1)
                if hero.hp <= 0:
                    print("++++++You were killed++++++")
                    break
                else:
                    continue
            else:
                print("++++++You killed " + mob.name + "++++++", "", sep="\n")
                print("Gained " + str(mob.exp) + "XP.", "", sep="\n")
                hero.loot()
                hero.EXP += mob.exp
                mob.hp = mob.MAX_HP
                if hero.EXP >= hero.LVL_EXP:
                    hero.level_up()
                    break
                time.sleep(1)
                break

    @staticmethod
    def prepare_spell():
        """ This method defines how the Player character cast spells. There is 50/50 chance that Player will
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

    @staticmethod
    def cast_spell():
        """ This method defines how Player character casts spell"""

        while True:
            Player.prepare_spell()
            if mob.hp > 0:
                Player.monster_attack()
                time.sleep(1)
                if hero.hp <= 0:
                    print("++++++You were killed++++++")
                    time.sleep(1)
                    break
                else:
                    from actions import battle
                    battle()
            else:
                print("++++++You killed " + mob.name + "++++++", "", sep="\n")
                print("Gained " + str(mob.exp) + "XP.", "", sep="\n")
                Player.loot()
                hero.EXP += mob.exp
                mob.hp = mob.MAX_HP
                if hero.EXP >= hero.LVL_EXP:
                    Player.level_up()
                    break
                else:
                    hero.hp = hero.MAX_HP
                time.sleep(1)
                break

    @staticmethod
    def check_stats():
        """ This method prints current Player character stats"""

        print("Name: {}, HP: {}, MANA: {}, AC: {}, EXP: {}, ATK: {}\n".format(
            hero.name, hero.hp, hero.mana, hero.ac, hero.EXP, hero.thaco))


class Fighter(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=12, ac=6, mana=0)

    def fight(self):
        super().fight()

    def heal(self):
        super().heal()

    def inventory(self):
        super().inventory()

    def check_equipment(self):
        super().check_equipment()

    def check_stats(self):
        super().check_stats()

    def equip(self):
        super().equip()

    PROF = "FIGHTER"
    MAX_HP = 12
    HD = 8
    LEVEL = 1
    EXP = 1
    LVL_EXP = 40
    MANA = 0
    MAX_MANA = 0
    ATK = 20
    COMMANDS = {
        'f': ('fight', fight),
        'h': ('heal', heal),
        'i': ('check inventory', inventory),
        'e': ('check equipment', check_equipment),
        'c': ('check stats', check_stats),
        'eq': ('equip item', equip)
    }

    INVENTORY = [heal_pot, heal_pot, short_sword, long_sword]


class Rogue(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=9, ac=4, mana=0)

    def fight(self):
        super().fight()

    def heal(self):
        super().heal()

    def inventory(self):
        super().inventory()

    def backstab(self):
        pass

    def check_equipment(self):
        super().check_equipment()

    def check_stats(self):
        super().check_stats()

    def equip(self):
        super().equip()

    PROF = "ROGUE"
    MAX_HP = 9
    HD = 6
    LEVEL = 1
    EXP = 15
    MANA = 0
    MAX_MANA = 0
    LVL_EXP = 10
    ATK = [1, 2, 3, 4, 5, 6, 7]
    COMMANDS = {
        'f': ('fight', fight),
        'b': ('backstab', backstab),
        'h': ('heal', heal),
        'i': ('check inventory', inventory),
        'e': ('check equipment', check_equipment),
        'c': ('check stats', check_stats),
        'eq': ('equip item', equip)
    }

    INVENTORY = []


class Mage(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=500, ac=7, mana=5)

    def fight(self):
        super().fight()

    def heal(self):
        super().heal()

    def inventory(self):
        super().inventory()

    def refresh_mana(self):
        super().refresh_mana()

    def cast_spell(self):
        super().cast_spell()

    def check_equipment(self):
        super().check_equipment()

    def check_stats(self):
        super().check_stats()

    def equip(self):
        super().equip()

    PROF = "MAGE"
    MAX_HP = 500
    HD = 4
    LEVEL = 1
    EXP = 15
    LVL_EXP = 100
    MANA = 5
    MAX_MANA = 5
    ATK = [1, 2, 3, 4]
    COMMANDS = {
        'f': ('fight', fight),
        's': ('cast spell', cast_spell),
        'm': ('restore mana', refresh_mana),
        'h': ('heal', heal),
        'i': ('check inventory', inventory),
        'e': ('check equipment', check_equipment),
        'c': ('check stats', check_stats),
        'eq': ('equip item', equip)
    }

    INVENTORY = [heal_pot, mana_pot, mana_pot, heal_pot, heal_pot, heal_pot]


def profession():
    while True:
        letter_to_profession = {
            'f': Fighter,
            'r': Rogue,
            'm': Mage
        }
        print("What is your class?\n")
        for letter in letter_to_profession.keys():
            print("- Press {} for {}".format(
                letter, letter_to_profession[letter].__name__))
        p_class = input(">>>")
        if p_class in letter_to_profession:
            return letter_to_profession[p_class]()
        else:
            print("You must choose a valid class...")
            continue


hero = profession()
slot = hero.EQUIPMENT_SLOTS
level_up_die = Die(hero.HD)
