#!/usr/bin/python3

class Spells:
    def __init__(self,name):
        self.name = name

class Fireball(Spells):
    def __init__(self):
        super().__init__(name="Fireball")

    DAMAGE = [5,10]
    MANA = 3

class Frostbolt(Spells):
    def __init__(self):
        super().__init__(name="Frostbolt")

    DAMAGE = [4,7]
    MANA = 2

class magic_missle(Spells):
    def __init__(self):
        super().__init__(name="magic_missle")

    DAMAGE = [2,3,4,5]
    MANA = 1


def choose_spell():
    while True:
        short_to_spell = {
            'fb': Fireball,
            'fsb': Frostbolt,
            'mm': magic_missle
        }
        print("Choose spell\n")
        for short in short_to_spell.keys():
            print("- Press {} for {}".format(
                short, short_to_spell[short].__name__))
        chooseSpell = input(">>>")
        if chooseSpell in short_to_spell:
            return short_to_spell[chooseSpell]()
            break
        else:
            print("You must choose a valid spell...")
            continue
