import random


class Monster:
    def __init__(self, name,hp,ac,exp,thaco):
        self.name = name
        self.hp = hp
        self.ac = ac
        self.exp = exp
        self.thaco = thaco

class Zombie(Monster):
    def __init__(self):
        super(Zombie, self).__init__(name="Zombie",
                                     hp=10, ac=10,
                                     exp=4, thaco=20)


    HP = 10
    AC = 10
    EXP = 4
    THACO = 20
    MAX_HP = 10
    ATK = [1, 2, 3, 4, 5, 6, 7]
    INVENTORY = ["MP Potion", "HP Potion", "Broken axe"]


class Ghul(Monster):
    def __init__(self):
        super(Ghul, self).__init__(name="Ghul",
                                   hp=12, ac=10,
                                   exp=1, thaco=20)

    INVENTORY = ["MP Potion", "HP Potion", "Hammer"]
    MAX_HP = 12
    ATK = [1, 2, 3, 4, 5, 6]


class Skeleton(Monster):
    def __init__(self):
        super(Skeleton, self).__init__(name="Skeleton",
                                       hp=6, ac=10,
                                       exp=1, thaco=20)

    INVENTORY = ["MP Potion", "HP Potion", "Mace"]
    MAX_HP = 6
    ATK = [1, 2, 3, 4]


class Ghost(Monster):
    def __init__(self):
        super(Ghost, self).__init__(name="Ghost",
                                    hp=5, ac=8,
                                    exp=2, thaco=20)

    INVENTORY = ["MP Potion", "HP Potion", "Axe"]
    MAX_HP = 5
    ATK = [1, 2, 3, 4, 5, 6]


class Slime(Monster):
    def __init__(self):
        super(Slime, self).__init__(name="Slime",
                                    hp=26, ac=8,
                                    exp=4, thaco=20)

    INVENTORY = ["MP Potion", "HP Potion", "Sword"]
    MAX_HP = 26
    ATK = [5, 6, 7, 8, 9, 10]


def random_mob():
    monster = [Zombie(), Ghul(), Ghost(), Skeleton(), Slime()]
    choose_mob = random.choice(monster)
    return choose_mob


mob = random_mob()