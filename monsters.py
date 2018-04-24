#!/usr/bin/python3

from dice import *

class Monster:
     def __init__(self,name,hp,ac,exp,thaco):
        self.name=name
        self.hp=hp
        self.ac=ac
        self.exp=exp
        self.thaco=thaco


class Zombie(Monster):
    def __init__(self):
        super().__init__(name="Zombie",
                         hp=10,ac=5,
                         exp=4,thaco=20)

    POWER=[1,2,3,4,5,6,7]

class Ghul(Monster):
    def __init__(self):
        super().__init__(name="Ghul",
                         hp=12,ac=6,
                         exp=1,thaco=20)

    POWER=[1,2,3,4,5,6]

class Skeleton(Monster):
    def __init__(self):
        super().__init__(name="Skeleton",
                         hp=6,ac=2,
                         exp=1,thaco=20)

    POWER=[1,2,3,4]

class Ghost(Monster):
    def __init__(self):
        super().__init__(name="Ghost",
                         hp=5,ac=10,
                         exp=2,thaco=20)

    POWER=[1,2,3,4,5,6]


class Slime(Monster):
    def __init__(self):
        super().__init__(name="Slime",
                         hp=26,ac=8,
                         exp=4,thaco=20)

    POWER=[5,6,7,8,9,10]

def random_mob():
    roll = twenty_sided_die.roll()
    if roll <= 5 :
        return Zombie()
    elif roll <= 10:
        return Ghul()
    elif roll <= 15:
        return Skeleton()
    elif roll <= 19:
        return Ghost()
    else:
        return Slime()

mob = random_mob()
