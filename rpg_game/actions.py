from professions import *


def battle():
    """ This function defines player character encounter with a random monster, depending of the chosen command,
    player / monster takes appropriate action """

    while True:
        for command, action in hero.COMMANDS.items():
            print("Press {} to {}".format(command, action[0]))
        command = input("~~~~~~~Press key to continue~~~~~~~")
        if command not in hero.COMMANDS:
            print("Not a valid command")
            continue
        else:
            if command == "i":
                hero.inventory()
                continue
            elif command == "h":
                hero.heal()
                continue
            elif command == "m":
                hero.generate_mana()
                continue
            elif command == "f":
                hero.fight()
            elif command == "s":
                hero.cast_spell()
        break
