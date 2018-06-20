class Armor:
    def __init__(self, name, DEF, slot):
        self.name = name
        self.ATK = DEF
        self.slot = slot


class LeatherArmor(Armor):
    super().__init__(name="Leather armor", DEF=1, slot="chest")


