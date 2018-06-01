class Sword:
    def __init__(self,name,ATK):
        self.name = name
        self.ATK = ATK


class ShortSword(Sword):
    def __init__(self):
        super(ShortSword, self).__init__(name="Short Sword",
                                         ATK=1)

    def __str__(self):
        return "Short Sword"


class LongSword(Sword):
    def __init__(self):
        super(LongSword, self).__init__(name="Long Sword",
                                        ATK=2)

    def __str__(self):
        return "Long Sword"


class BastardSword(Sword):
    def __init__(self):
        super(BastardSword, self).__init__(name="Bastard Sword",
                                           ATK=3)

    def __str__(self):
        return "Bastard Sword"


class TwoHandedSword(Sword):
    def __init__(self):
        super(TwoHandedSword, self).__init__(name="Two Handed Sword",
                                             ATK=5)

    def __str__(self):
        return "Two Handed Sword"


short_sword = ShortSword().__str__()
long_sword = LongSword().__str__()
bastard_sword = BastardSword().__str__()
two_handed_sword = TwoHandedSword().__str__()