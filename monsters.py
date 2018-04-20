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
                         exp=5,thaco=20)

class Ghul(Monster):
    def __init__(self):
        super().__init__(name="Ghul",
                         hp=12,ac=6,
                         exp=4,thaco=20)

class Skeleton(Monster):
    def __init__(self):
        super().__init__(name="Skeleton",
                         hp=6,ac=2,
                         exp=2,thaco=20)

class Ghost(Monster):
    def __init__(self):
        super().__init__(name="Ghost",
                         hp=5,ac=10,
                         exp=5,thaco=20)

def random_mob():
    mob=Zombie() if four_sided_die.roll()>2 else Ghul()
    return mob

mob = random_mob()
