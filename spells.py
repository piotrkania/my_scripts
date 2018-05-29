class Spells:
    def __init__(self,name):
        self.name = name


class Fireball(Spells):
    def __init__(self):
        super().__init__(name="Fireball")

    DAMAGE = [1]
    MANA = 3


class Frostbolt(Spells):
    def __init__(self):
        super().__init__(name="Frostbolt")

    DAMAGE = [4, 5]
    MANA = 2


class magic_missile(Spells):
    def __init__(self):
        super().__init__(name="magic_missile")

    DAMAGE = [2, 3, 4, 5]
    MANA = 1


def choose_spell():
    while True:
        short_to_spell = {
            'fb': Fireball,
            'fsb': Frostbolt,
            'mm': magic_missile
        }
        print("Choose spell\n")
        for short in short_to_spell.keys():
            print("- Press {} for {}".format(
                short, short_to_spell[short].__name__))
        pick_spell = input(">>>")
        if pick_spell in short_to_spell:
            return short_to_spell[pick_spell]()
        else:
            print("You must choose a valid spell...")
            continue
