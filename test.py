#!/usr/bin/python3

import welcome
from actions import PlayerAttack
from dice import Die
from professions import Fighter
from professions import Rogue
from professions import Mage
from monsters import Zombie
from monsters import Ghul
from monsters import Ghost
from monsters import Skeleton
import races
import spells

# defines types of dice
four_sided_die=Die(4)
six_sided_die=Die(6)
ten_sided_die=Die(10)
twenty_sided_die=Die(20)


# Function to provide characters race
def char_race():
     race_list=['Orc','Human','Elf','Dwarf']
     while True:
        race=input("Please select Your race (Orc/Elf/Human/Dwarf): ")
        if race.isalpha() and race in race_list:
            return race
        else:
            print("You must choose a valid race!")
            continue


# Function to choose first chamber
def first_chamber():
    while True:
        first_chamber={
        'Left': 'Military quarters. Watch out for undead troops!!!',
        'Center': 'Cellar. Something or someone can eat You here...Watch Your back...',
        'Right': 'Servants quarters. Whats crawling below?'
}
        direction=input("Where would You like to go? (Left/Right/Center): ")
        for key in first_chamber.items():
            if direction in first_chamber:
                return first_chamber[direction]
            else:
                print("Wrong direction, choose again...")
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
        print("Rolled " + str(roll) + "." +  "You hit the monster\n" )
        if hero.PROF==Fighter:
            rollD=ten_sided_die.roll()

        if hero.PROF==Rogue:
            rollD=six_sided_die.roll()

        if hero.PROF==Mage:
            rollD=four_sided_die.roll()
    else:
       print("Rolled " + str(roll) + "." + "You missed")




# Race selection

var_race=char_race()
if var_race=='Orc':
    print("""



You yawn widely, and scratch Your head. 'What happend yesterday? I can't remember anything...
Last moment, last thing that I remember was this...person...thing...
Who or what was that?'....
...
...
...
...
...

You see an old Orc Shaman, with only one eye.
He's old, very old, even for orcish standards.
'You come, me got gift for you' - screamed the old Orc.
A sudden an unknown curiosity forced You to move towards him.
'You take, no ask'
The same curiosity told You to take the gift - strange looking key,
with a strange, fiendish skull.
'You know where, You sleep now' yelled the Shaman and when You started
to realize whats happening, darkness came and You fell asleep.
You woke up, near a strange looking mansion, with a key in Your pocket.
'What the hell is going on?'
Driven by the same feeling You had earlier, You take Your axe and start
walking towards the building.




""")
elif var_race=='Elf':
    print("""

You wake up in Your house, deep in the woods.
First lights of the autumn sun are slowly shining through the trees.
You haven't slept well, all night driven by nightmares...
But was it only a nightmare?...
...
...
...
...
...

You were chasing a strange looking creature, twisted and vile.
For sure it wasn't something from this realm - dark red skin,
long arms, short legs. Claws that could rip to shredds anything they catch.
And those eyes - two frenzied fiery dots, which could fear every brave mortal.
'Where did it came from? What this foul creature is doing here?
I must not let it escape.'
You were sending arrow after arrow, each shot closer to the target.
'This creature is fast!' - You moaned.
Suddenly it stopped just for a second, but that was enough to hit it in its head.
You smiled to yourself and walked to the corpse.
The creature had something in its hand - map and a strange looking key with a fiendish skull.
'What is this? Where does this map....' - dream ends.
...
...
...
...
'It was only a dream, nothing more.'
You get up from the bed and look at the table.
KEY!!!! The same key from your dream.
And the map, showig direction to a strange looking mansion
You dont know why, but took Your equipment and followed the map.
After few days, you reached the house.
'Why am I here?'
You slowly walk towards the door...

""")
elif var_race=='Dwarf':
    print("Dwarvish")
elif var_race=='Human':
    print("Humanish")

# Profession selection

hero = profession()
print("Name: {}, HP: {}, AC: {}, EXP: {}, ATK: {}\n".format(
      hero.name, hero.hp, hero.ac, hero.exp, hero.thaco))


# Enter the building

while True:
    start=input("Hit 'Enter' to enter the building: ")
    if start=="":
        print("You slowly enter the mansion")
        break
    else:
        print("Are You sure You dont't want to know whats behind the door ?")
        continue


# Events based on first chamber selection
var_firstChamber=first_chamber()
print(var_firstChamber)

mob=random_mob()

for command, action in hero.COMMANDS.items():
    print("Press {} to {}".format(command, action[0]))

while True:
    command = input("~~~~~~~Press key to continue~~~~~~~")
    if command not in hero.COMMANDS:
        print("Not a valid command")
        continue
    break
print("You are fighting "  + mob.name)

if command:
    hero.COMMANDS[command][1]()
    PlayerAttack()

    
    
#   Dla kazdego spella utworzyc klase, wpisac tam atrybuty, w pozniejszej faze stworzy klasy dla kazdej
#   z ras + atrybuty, przy wyborze profesji suma stat rasa+profesja, utworzyc ekwipunek, dodac potiony itd itp 
