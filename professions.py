#!/usr/bin/python3

class Player:
    def __init__(self,name,hp,ac,exp,thaco):
        self.name=name
        self.hp=hp
        self.ac=ac
        self.exp=exp
        self.thaco=thaco

class Fighter(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=12,ac=10,
                         exp=10,thaco=20)
    def fight():
        pass

    PROF="FIGHTER"
    MAX_HP=12
    HD=8
    LEVEL_2=20
    COMMANDS = {
        'f' : ('fight', fight)
    }

class Rogue(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=9,ac=10,
                         exp=10,thaco=20)

    def fight():
        pass
    def backstab():
        pass

    PROF="ROGUE"
    MAX_HP=9
    HD=6
    LEVEL_2=15
    COMMANDS = {
        'f' : ('fight', fight),
        'b' : ('backstab', backstab)
    }



class Mage(Player):
    def __init__(self):
        super().__init__(name=input("Whats Your name?: "),
                         hp=12,ac=10,
                         exp=10,thaco=20)

    def fight():
        pass

    def generate_mana():
        pass

    def cast_spell():
        pass

    PROF="MAGE"
    MAX_HP=5
    HD=4
    LEVEL_2=10
    MANA=1
    MAX_MANA=1
    COMMANDS = {
        'f' : ('fight', fight),
        's' : ('spell', cast_spell),
        'm' : ('mana', generate_mana)
    }



