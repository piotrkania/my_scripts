class Potion:
    def __init__(self, name, type, value):
        self.name = name
        self.type = type
        self.value = value


class HpPotion(Potion):
    def __init__(self):
        super().__init__(name="HP Potion", type="heal",
                         value=5)

    HP = 3

    def __str__(self):
        return str(self.name)


class MpPotion(Potion):
    def __init__(self):
        super().__init__(name="MP Potion", type="mana",
                         value=5)

    MP = 3

    def __str__(self):
        return str(self.name)


heal_pot = HpPotion()
mana_pot = MpPotion()
