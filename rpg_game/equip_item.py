from actions import *


def equip_hand():
    print("Press {} to equip Short sword".format('s'))
    print("Press {} to equip Long sword".format('l'))
    print("Press {} to equip Bastard sword".format('b'))
    weap = input(">>>>")
    from actions import battle
    if weap == 's':
        while short_sword in hero.INVENTORY:
            for k,v in hero.EQUIPMENT_SLOTS.items():
                for n in v:
                    if n == "Long Sword":
                        hero.INVENTORY.append(long_sword)
                        hero.EQUIPMENT_SLOTS.update({'Hand': short_sword})
                        print(hero.ATK)
                        hero.INVENTORY.remove(short_sword)
                        print("Your ATK increased by " + str(short_sword.ATK))
                        battle()
                    else:
                        hero.EQUIPMENT_SLOTS.update({'Hand': short_sword})
                    print(hero.ATK)
                    hero.INVENTORY.remove(short_sword)
                    print("Your ATK increased by " + str(short_sword.ATK))
                    battle()
        else:
            print("You do not have it in Your inventory")
            battle()
    elif weap == "l":
        while long_sword in hero.INVENTORY:
            hero.EQUIPMENT_SLOTS.update({'Hand': long_sword})
            hero.ATK += long_sword.ATK
            hero.INVENTORY.remove(long_sword)
            print("Your ATK increased by " + str(long_sword.ATK))
            battle()
        else:
            print("You do not have it in Your inventory")
            battle()
    elif weap == "b":
        while bastard_Sword in hero.INVENTORY:
            hero.EQUIPMENT_SLOTS.update({'Hand': bastard_Sword})
            hero.ATK += bastard_Sword.ATK
            hero.INVENTORY.remove(bastard_Sword)
            print("Your ATK increased by " + str(bastard_Sword.ATK))
            battle()
        else:
            print("You do not have it in Your inventory")
            battle()