# libraries
import health_points
import characters
import experience

# function dead
def dead(character):
    # player dead
    if character.name == characters.player.name:
        print(f"Your health points: {character.hp}/{character.hp_max}")
        print("You are dead! Game over!")
        print("")
        exit(0)
    # enemy dead
    else:
        print(f"Health points {character.name}: {character.hp}/{character.hp_max}")
        print(f"{character.name} is dead. You win!")
        print("")
        experience.exp(character.ep)
        print("")
