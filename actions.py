#!/usr/bin/python3


class Player:
    def __init__(self,name,hp,ac,thaco):
        self.name=name
        self.hp=hp
        self.ac=ac
        self.thaco=thaco

class Fighter(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=12,ac=6,
                         thaco=20)
    def fight():
        pass

    PROF="FIGHTER"
    MAX_HP=12
    HD=8
    LEVEL=1
    EXP=1
    LVL_EXP=4
    POWER=[20]
    COMMANDS = {
        'f' : ('fight', fight)
    }

class Rogue(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=9,ac=4,
                         thaco=20)

    def fight():
        pass
    def backstab():
        pass

    PROF="ROGUE"
    MAX_HP=9
    LEVEL=1
    LEVEL_2=15
    POWER=[1-7]
    COMMANDS = {
        'f' : ('fight', fight),
        'b' : ('backstab', backstab)
    }



class Mage(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=12,ac=7,
                         thaco=20)

    def fight():
        pass

    def generate_mana():
        pass

    def cast_spell():
        pass

    PROF="MAGE"
    MAX_HP=5
    LEVEL=1
    LEVEL_2=10
    MANA=1
    MAX_MANA=1
    POWER=[1,2,3,4]
    COMMANDS = {
        'f' : ('fight', fight),
        's' : ('spell', cast_spell),
        'm' : ('mana', generate_mana)
    }

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
        pclass = input(">>>")
        if pclass in letter_to_profession:
            return letter_to_profession[pclass]()
            break
        else:
            print("You must choose a valid class...")
            continue

hero = profession()
