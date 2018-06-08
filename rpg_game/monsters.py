import random
from potions import *


class Monster:
    def __init__(self, ac, exp, hp, name, **kwargs):
        self.thaco = 20
        self.kwargs = kwargs
        self.ac = ac
        self.exp = exp
        self.hp = hp
        self.name = name


class Zombie(Monster):
    def __init__(self):
        super(Zombie, self).__init__(name="Zombie",
                                     hp=10, ac=10,
                                     exp=4)

    MAX_HP = 10
    ATK = [1, 2, 3, 4, 5, 6, 7]
    INVENTORY = [heal_pot, mana_pot]

    def __str__(self):
        return "Zombie"


class Ghul(Monster):
    def __init__(self):
        super(Ghul, self).__init__(name="Ghul",
                                   hp=12, ac=10,
                                   exp=1)

    INVENTORY = [heal_pot, mana_pot]
    MAX_HP = 12
    ATK = [1, 2, 3, 4, 5, 6]

    def __str__(self):
        return "Ghul"


class Skeleton(Monster):
    def __init__(self):
        super(Skeleton, self).__init__(name="Skeleton",
                                       hp=6, ac=10,
                                       exp=1)

    INVENTORY = [heal_pot, mana_pot]
    MAX_HP = 6
    ATK = [1, 2, 3, 4]

    def __str__(self):
        return "Skeleton"


class Ghost(Monster):
    def __init__(self):
        super(Ghost, self).__init__(name="Ghost",
                                    hp=5, ac=8,
                                    exp=2)

    INVENTORY = [heal_pot, mana_pot]
    MAX_HP = 5
    ATK = [1, 2, 3, 4, 5, 6]

    def __str__(self):
        return "Ghost"


class Slime(Monster):
    def __init__(self):
        super(Slime, self).__init__(name="Slime",
                                    hp=26, ac=8,
                                    exp=4)

    INVENTORY = [heal_pot, mana_pot]
    MAX_HP = 26
    ATK = [5, 6, 7, 8, 9, 10]

    def __str__(self):
        return "Slime"


class MobFactory(Monster):
    @staticmethod
    def random_mob():
        monster = [Zombie(), Ghul(), Ghost(), Skeleton(), Slime()]
        choose_mob = random.choice(monster)
        return choose_mob


def encounter():
    mobs = MobFactory.random_mob()
    return mobs


mob = encounter()
