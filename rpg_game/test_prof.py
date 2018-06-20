from weapons import *
from professions import *
from actions import *

slot = hero.EQUIPMENT_SLOTS


def equip():
    n = 0
    while True:
        for k in slot.keys():
            n += 1
            print("Press {} to equip {}".format(n, '%s' % k))
        option = input("Choose slot You wish to equip >>>>> ")
        if option == "10":
            equip_hand()
        else:
            print("Choose the correct slot")
            continue


def equip_hand():
    print("Press {} to equip Short sword".format('s'))
    print("Press {} to equip Long sword".format('l'))
    print("Press {} to equip Bastard sword".format('b'))
    weap = input(">>>>")
    if weap == 's':
        while short_sword in hero.INVENTORY:
            hero.ATK += short_sword.ATK
            hero.INVENTORY.remove(short_sword)
            slot.
            print("Your hero attack increased by " + str(short_sword.ATK))
            battle()
        else:
            print("You do not have it in Your inventory")
    elif weap == "l":
        while long_sword in hero.INVENTORY:
            hero.ATK += long_sword.ATK
            hero.INVENTORY.remove(long_sword)
            print("Your hero attack increased by " + str(long_sword.ATK))
            battle()
            break
        else:
            print("You do not have it in Your inventory")
    elif weap == "b":
        while bastard_Sword in hero.INVENTORY:
            hero.ATK += bastard_Sword.ATK
            hero.INVENTORY.remove(bastard_Sword)
            print("Your hero attack increased by " + str(bastard_Sword.ATK))
            battle()
            break
        else:
            print("You do not have it in Your inventory")


equip()

