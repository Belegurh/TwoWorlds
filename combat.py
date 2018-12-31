# libraries
import random
import health_points
import weapons
import characters


# 0 = normal combat flee-mode
# 1 = story flee-mode Dev Lands
flee_mode = 0


# initialize fight
def init_fight(num_fighter, enemy):
    print(" _____________________")
    print("|                     |")
    print("| <<< Combat Mode >>> |")
    print("|_____________________|")
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
        print("Make a move! 'attack' or 'flee'?")
        choice = input("> ")
        if "attack" in choice:
            attack_player(weapons.applied_weapon, enemy)
            break
        elif "flee" in choice:
            flee_player()
            break
        else:
            continue


# player, attack
def attack_player(weapon, enemy):
    print("")
    print(f"You attack the {enemy.name} with '{weapon.name}'!")
    health_points.health(weapon.demage, enemy)
    print("_____________________________________________________________")
    input("Press Enter to countinue...")
    attack_enemy(enemy)


# enemy, attack
def attack_enemy(enemy): #characters.hellhound
    print("")
    print(f"{enemy.name} attacks with \"{enemy.weapon}\".")
    health_points.health(enemy.demage, characters.player)
    print("_____________________________________________________________")
    aktion_player(enemy)


# player, flee
def flee_player():
    if flee_mode == 1:
        print("")
    else:
        print("normal cambat flee-mode. Program me please!!")
