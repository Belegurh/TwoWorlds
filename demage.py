import weapons
import characters
import random

def rnd_dmg(character, weapon):
    dmg_max = (character.strength * -1) + weapon.demage
    # print(f"max_dmg: {dmg_max}")
    dmg_min = int(dmg_max * 0.5)
    # print(f"min_dmg: {dmg_min}")

    return random.randint(dmg_max, dmg_min)