class Player:
    def __init__(self, name, hp, ac, mana, thaco):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.mana = mana
        self.thaco = thaco


class Fighter(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=12, ac=6, mana=0,
                         thaco=20)

    def fight():
        pass

    def inventory():
        pass

    def heal():
        pass

    PROF = "FIGHTER"
    MAX_HP = 12
    HD = 8
    LEVEL = 1
    EXP = 1
    LVL_EXP = 4
    MANA = 0
    MAX_MANA = 0
    ATK = [20]
    COMMANDS = {
        'f': ('fight', fight),
        'h': ('heal', heal),
        'i': ('inventory', inventory)
    }

    INVENTORY = []


class Rogue(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=9, ac=4, mana=0,
                         thaco=20)

    def fight():
        pass

    def backstab():
        pass

    def inventory():
        pass

    def heal():
        pass

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
        'i': ('inventory', inventory)
    }

    INVENTORY = []


class Mage(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=700, ac=7, mana=5,
                         thaco=20)

    def fight():
        pass

    def generate_mana():
        pass

    def cast_spell():
        pass

    def inventory():
        pass

    def heal():
        pass

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
        's': ('spell', cast_spell),
        'm': ('mana', generate_mana),
        'h': ('heal', heal),
        'i': ('inventory', inventory)
    }

    INVENTORY = []


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
        else:
            print("You must choose a valid class...")
            continue


hero = profession()
