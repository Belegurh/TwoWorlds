# libraries
import char_dead

# change health points. if hp > hp_max, hp = hp_max. Insert the additional hp as argument
def health(change_hp, character):

    if ((character.hp + change_hp) <= character.hp_max) and (character.hp + change_hp > 0):
        character.hp += change_hp
        if change_hp >= 0:
            print(f"hp + {change_hp}")
        else:
            print("hp -", change_hp * -1, f", Health points {character.name}: {character.hp}/{character.hp_max}")
    elif character.hp + change_hp > character.hp_max:
        character.hp = character.hp_max
        print(f"hp + {change_hp}, Health points {character.name}: {character.hp}/{character.hp_max}")
    elif character.hp + change_hp <= 0:
        character.hp += change_hp
        print("hp -", change_hp * -1)
        char_dead.dead(character)
    else:
        print(">>>failure, wrong hp! Please contact your admin!<<<")
