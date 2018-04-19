#!/usr/bin/python3

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
