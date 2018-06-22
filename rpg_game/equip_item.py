from actions import *


def equip_hand():
    print("Press {} to equip Short sword".format('s'))
    print("Press {} to equip Long sword".format('l'))
    print("Press {} to equip Bastard sword".format('b'))
    weap = input(">>>>")
    if weap == 's':
        while short_sword in hero.INVENTORY:
            if hero.EQUIPMENT_SLOTS['Hand'] == long_sword:
                hero.INVENTORY.append(long_sword)
                hero.ATK -= long_sword.ATK
                hero.INVENTORY.remove(short_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': short_sword})
                hero.ATK += short_sword.ATK
                print("Your ATK increased by " + str(short_sword.ATK))
                battle()
            elif hero.EQUIPMENT_SLOTS['Hand'] == bastard_Sword:
                hero.INVENTORY.append(bastard_Sword)
                hero.ATK -= bastard_Sword.ATK
                hero.INVENTORY.remove(short_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': short_sword})
                hero.ATK += short_sword.ATK
                print("Your ATK increased by " + str(short_sword.ATK))
                battle()
            elif hero.EQUIPMENT_SLOTS['Hand'] == two_handed_sword:
                hero.INVENTORY.append(two_handed_sword)
                hero.ATK -= two_handed_sword.ATK
                hero.INVENTORY.remove(short_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': short_sword})
                hero.ATK += short_sword.ATK
                print("Your ATK increased by " + str(short_sword.ATK))
                battle()
            else:
                hero.ATK += short_sword.ATK
                hero.INVENTORY.remove(short_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': short_sword})
                hero.ATK += short_sword.ATK
                print("Your ATK increased by " + str(short_sword.ATK))
                battle()
        else:
            print("You do not have it in Your inventory")
            battle()
    elif weap == "l":
        while long_sword in hero.INVENTORY:
            if hero.EQUIPMENT_SLOTS['Hand'] == short_sword:
                hero.INVENTORY.append(short_sword)
                hero.ATK -= short_sword.ATK
                hero.INVENTORY.remove(long_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': long_sword})
                hero.ATK += long_sword.ATK
                print("Your ATK increased by " + str(long_sword.ATK))
                battle()
            elif hero.EQUIPMENT_SLOTS['Hand'] == bastard_Sword:
                hero.INVENTORY.append(bastard_Sword)
                hero.ATK -= bastard_Sword.ATK
                hero.INVENTORY.remove(long_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': long_sword})
                hero.ATK += long_sword.ATK
                print("Your ATK increased by " + str(long_sword.ATK))
                battle()
            elif hero.EQUIPMENT_SLOTS['Hand'] == two_handed_sword:
                hero.INVENTORY.append(two_handed_sword)
                hero.ATK -= two_handed_sword.ATK
                hero.INVENTORY.remove(long_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': long_sword})
                hero.ATK += long_sword.ATK
                print("Your ATK increased by " + str(long_sword.ATK))
                battle()
            else:
                hero.INVENTORY.remove(long_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': long_sword})
                hero.ATK += long_sword.ATK
                print("Your ATK increased by " + str(short_sword.ATK))
                battle()
        else:
            print("You do not have it in Your inventory")
            battle()
    elif weap == "b":
        while bastard_Sword in hero.INVENTORY:
            if hero.EQUIPMENT_SLOTS['Hand'] == short_sword:
                hero.INVENTORY.append(short_sword)
                hero.ATK -= short_sword.ATK
                hero.INVENTORY.remove(bastard_Sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': bastard_Sword})
                hero.ATK += bastard_Sword.ATK
                print("Your ATK increased by " + str(bastard_Sword.ATK))
                battle()
            elif hero.EQUIPMENT_SLOTS['Hand'] == long_sword:
                hero.INVENTORY.append(long_sword)
                hero.ATK -= long_sword.ATK
                hero.INVENTORY.remove(bastard_Sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': bastard_Sword})
                hero.ATK += bastard_Sword.ATK
                print("Your ATK increased by " + str(bastard_Sword.ATK))
                battle()
            elif hero.EQUIPMENT_SLOTS['Hand'] == two_handed_sword:
                hero.INVENTORY.append(two_handed_sword)
                hero.ATK -= two_handed_sword.ATK
                hero.INVENTORY.remove(bastard_Sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': bastard_Sword})
                hero.ATK += bastard_Sword.ATK
                print("Your ATK increased by " + str(bastard_Sword.ATK))
                battle()
            else:
                hero.INVENTORY.remove(bastard_Sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': bastard_Sword})
                hero.ATK += bastard_Sword.ATK
                print("Your ATK increased by " + str(bastard_Sword.ATK))
                battle()
        else:
            print("You do not have it in Your inventory")
            battle()
    elif weap == "t":
        while two_handed_sword in hero.INVENTORY:
            if hero.EQUIPMENT_SLOTS['Hand'] == short_sword:
                hero.INVENTORY.append(short_sword)
                hero.ATK -= short_sword.ATK
                hero.INVENTORY.remove(two_handed_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': two_handed_sword})
                hero.ATK += two_handed_sword.ATK
                print("Your ATK increased by " + str(two_handed_sword.ATK))
                battle()
            elif hero.EQUIPMENT_SLOTS['Hand'] == long_sword:
                hero.INVENTORY.append(long_sword)
                hero.ATK -= long_sword.ATK
                hero.INVENTORY.remove(two_handed_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': two_handed_sword})
                hero.ATK += two_handed_sword.ATK
                print("Your ATK increased by " + str(two_handed_sword.ATK))
                battle()
            elif hero.EQUIPMENT_SLOTS['Hand'] == bastard_Sword:
                hero.INVENTORY.append(bastard_Sword)
                hero.ATK -= bastard_Sword.ATK
                hero.INVENTORY.remove(two_handed_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': two_handed_sword})
                hero.ATK += two_handed_sword.ATK
                print("Your ATK increased by " + str(two_handed_sword.ATK))
                battle()
            else:
                hero.INVENTORY.remove(two_handed_sword)
                hero.EQUIPMENT_SLOTS.update({'Hand': two_handed_sword})
                hero.ATK += two_handed_sword.ATK
                print("Your ATK increased by " + str(two_handed_sword.ATK))
                battle()
        else:
            print("You do not have it in Your inventory")
            battle()