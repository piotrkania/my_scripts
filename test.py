#!/usr/bin/python3

from random import randint



# Class to define die roll
class Die:
    def __init__(self, sides=6):
        self.sides = sides

    def roll(self):
        return randint(1, self.sides)

four_sided_die=Die(4)
six_sided_die=Die(6)
ten_sided_die=Die(10)
twenty_sided_die=Die(20)


class Player:
    def __init__(self,name,hp,ac,exp,thaco):
        self.name=name
        self.hp=hp
        self.ac=ac
        self.exp=exp
        self.thaco=thaco


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
                         exp=6,thaco=20)

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



def random_mob():
    mob=Zombie() if four_sided_die.roll()>2 else Ghul()
    return mob


def profession():
    while True:
        letter_to_profession = {
            'f': Fighter,
            'r': Rogue,
            'm': Mage
        }
        print("What is your class?\n")
        for letter in letter_to_profession.keys():
            print("- Press {} for {}".format(
                letter, letter_to_profession[letter].__name__))
        pclass = input(">>>")
        if pclass in letter_to_profession:
            return letter_to_profession[pclass]()
            break
        else:
            print("You must choose a valid class...")
            continue


def PlayerAttack():
    roll=twenty_sided_die.roll()
    if roll >= hero.thaco-mob.ac:
        print("Rolled " + str(roll) + "." +  "You hit the monster" )
        if hero.PROF==Fighter:
            rollD=ten_sided_die.roll()

        if hero.PROF==Rogue:
            rollD=six_sided_die.roll()

        if hero.PROF==Mage:
            rollD=four_sided_die.roll()
    else:
       print("You missed")
hero = profession()

print("Name: {}, HP: {}, AC: {}, EXP: {}, ATK: {}\n".format(
      hero.name, hero.hp, hero.ac, hero.exp, hero.thaco))

for command, action in hero.COMMANDS.items():
    print("Press {} to {}".format(command, action[0]))

while True:
    command = input("~~~~~~~Press key to continue~~~~~~~")
    if command and command not in hero.COMMANDS:
        print("Not a valid command")
        continue
    break
print("You are fighting " + mob.name)
if command:
    hero.COMMANDS[command][1]()
    PlayerAttack()

    
    
#   Dla kazdego spella utworzyc klase, wpisac tam atrybuty, w pozniejszej faze stworzy klasy dla kazdej
#   z ras + atrybuty, przy wyborze profesji suma stat rasa+profesja, utworzyc ekwipunek, dodac potiony itd itp 
