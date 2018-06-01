class Potion:
    def __init__(self, name):
        self.name = name


class HpPotion(Potion):
    def __init__(self):
        super().__init__(name="HP Potion")

    HP = 3

    def __str__(self):
        return str(self.name)


class MpPotion(Potion):
    def __init__(self):
        super().__init__(name="MP Potion")

    MP = 3

    def __str__(self):
        return str(self.name)


heal_potion = HpPotion().__str__()
mana_potion = MpPotion().__str__()
