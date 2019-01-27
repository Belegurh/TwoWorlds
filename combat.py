# libraries
import random
import health_points
import weapons
import characters
import damage
import time

# 0 = normal combat flee-mode
# 1 = story flee-mode Dev Lands
flee_mode = 0


# initialize fight
def init_fight(num_fighter, enemy):
    print(" ________________________")
    print("|                        |")
    print("| <<< Combat Mode On >>> |")
    print("|________________________|")
    print("")
    start_fight(num_fighter, enemy)


# random, who opens the fight.
# Player is num 0 (Example: 2 fighter. Function chooses between 0 and 1)
def start_fight(num_fighter, enemy):
     rnd_num = random.randrange(num_fighter)
     if rnd_num == 0:
         print(">>> You begin! <<<")
         print("")
         input("Press Enter to countinue...")
         aktion_player(enemy)
     else:
         print(f">>> {enemy.name} begins! <<<")
         print("")
         input("Press Enter to countinue...")
         attack_enemy(enemy)


# attack or flee
def aktion_player(enemy):
    while True:
        print("")
        print("Make a move! 'attack', 'flee' or 'uses item'?")
        choice = input("> ").lower()
        if "attack" in choice:
            attack_player(weapons.applied_weapon, enemy)
            break
        elif "flee" in choice:
            flee_player()
            break
        elif "item" in choice:
            print("Are you kidding me? I'm not programed yet! Just attack, you coward!")
        else:
            continue


# player, attack
def attack_player(weapon, enemy):
    print("")
    print(f"You attack the {enemy.name} with '{weapon.name}'!")
    health_points.health(damage.rnd_dmg(characters.player, weapons.applied_weapon), enemy)
    print("_____________________________________________________________")
    input("Press Enter to countinue...")
    if enemy.hp > 0:
        attack_enemy(enemy)
    else:
        print(" __________________________")
        print("|                          |")
        print("| <<< Combat Mode Off >>>  |")
        print("|__________________________|")
        print("")
        input("Press Enter to countinue...")


# enemy, attack
def attack_enemy(enemy): #characters.hellhound
    print("")
    print(f"{enemy.name} attacks with \"{enemy.weapon}\".")
    health_points.health(damage.rnd_dmg(enemy, weapons.weapon_enemy_1), characters.player)
    print("_____________________________________________________________")
    if flee_mode == 1 and characters.player.hp < 10:
        lost()
    else:
        aktion_player(enemy)


# player, flee
def flee_player():
    if flee_mode == 1:
        print("You flee in panic. You crash down a hill and lose your consciousness!")
    else:
        print("Normal cambat flee-mode. Program me please!!")


def lost():
    print("The Hellhound strikes you so hard that you lose your consciousness.")
    print("You fell to the ground. The last thing you can see is the attacking Hellhound... Blood splashes to the ground!")
    time.sleep(5)