class Sword:
    def __init__(self, name, ATK, type):
        self.name = name
        self.ATK = ATK
        self.type = type


class ShortSword(Sword):
    def __init__(self):
        super(ShortSword, self).__init__(name="Short Sword",
                                         ATK=10, type="weapon")

    def __str__(self):
        return str(self.name)


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__(name="Long Sword",
                                        ATK=1, type="weapon")

    def __str__(self):
        return str(self.name)


class BastardSword(Sword):
    def __init__(self):
        super(BastardSword, self).__init__(name="Bastard Sword",
                                           ATK=3, type="weapon")

    def __str__(self):
        return str(self.name)


class TwoHandedSword(Sword):
    def __init__(self):
        super(TwoHandedSword, self).__init__(name="Two Handed Sword",
                                             ATK=5, type="weapon")

    def __str__(self):
        return str(self.name)


short_sword = ShortSword()
long_sword = LongSword()
bastard_Sword = BastardSword()
two_handed_sword = TwoHandedSword()
