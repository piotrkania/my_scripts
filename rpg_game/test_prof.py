
def CastSpell():
    """ This function defines how the spells are being generated and casted by player character """

    while True:
        roll = four_sided_die.roll()
        spell = choose_spell()
        if hero.mana > spell.MANA:
            if roll <= 2:
                print(hero.name + " rolled " + str(roll) + " and successfuly concentrated to prepare a spell", "",
                      sep="\n")
                spelld = random.choice(spell.DAMAGE)