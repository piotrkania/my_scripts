from professions import *


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
            print(hero.ATK)
            from actions import *
            battle()
        else:
            print("You do not have it in Your inventory")
    elif weap == "l":
        while long_sword in hero.INVENTORY:
            hero.ATK += long_sword.ATK
            hero.INVENTORY.remove(long_sword)
            print(hero.ATK)
            break
        else:
            print("You do not have it in Your inventory")
    elif weap == "b":
        while bastard_Sword in hero.INVENTORY:
            hero.ATK += bastard_Sword.ATK
            hero.INVENTORY.remove(bastard_Sword)
            print(hero.ATK)
            break
        else:
            print("You do not have it in Your inventory")


equip()

