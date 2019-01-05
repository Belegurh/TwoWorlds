# libraries
import time
import random
import heal_items
import health_points
import experience
import combat
import weapons
import characters


# lists
bag = ["pen", "sandwich", "penny", "bottle"]
bag_new = []
random_item_oak = ["beautyfull leaf of the oak", "baseball", "used chewing gum", "hairclip"]


def start():
    print("")
    print("You sit in your classroom and stare out of the window.")
    print("Some birds are surrounding the mighty oak on the school yard.")
    print('Suddenly you can hear a whisper: "Hallo, can you hear me?"')

    while True:
        choice = input("> ").lower()
        if choice == "yes":
            talk_classroom()
        else:
            print("\"Hallo, can you here me?\"")


def talk_classroom():
    print("\"Wow, that is great. I didn't expect it to work! Please seek a lonely place where we can talk.\"")
    print("Do you want to go to the toilet or the oak?")

    while True:
        choice = input("> ").lower()
        if "toilet" in choice:
            toilet()
        elif "oak" in choice:
            oak()
        else:
            print("Please go to the toilet or the oak.")


def toilet():
    print("")
    print("You stand up and go to the toilet.")
    print("After you entered the rooom, you recognize that you are not alone.")
    print('"Damn, I should go to the oak."')
    print("")
#    time.sleep(12)
    oak()


def oak():
    print("")
    print("After you passed through the school, you arrive at the oak.")
    print("The sun is shining and you can smell the fragrance of the flowers.")
    print('"What a beautyfull day."')
    print("While you wait, you can see something glowing at the trunk of the tree.")
    print('"What is that?"')
    print("You explore the glowing.")
#    time.sleep(25)
    print('"It looks like a keyhole."')
    print('"Maybe I can stick something into it."')
    print("You open your bag and search for something helpful.")
    print(f"\"Let's see... The following items are in my bag.\" {bag}")
    print("")
#    time.sleep(15)
    choice_oak()


def choice_oak():
    print("Do you want to use any of your items?")

    while True:
        choice = input("> ").lower()

        if choice == "yes":
            try_item_oak()
        elif choice == "no":
            print("\"Ok, let's see if I can find something else.\"")
            print("")
            search_item_oak()
        else:
            print("yes or no?")


def try_item_oak():
    print("Which of your items do you want to use?")

    while True:
        item_oak = input("> ").lower()

        if item_oak == "pen":
            false_item_oak("pen")
        elif item_oak == "sandwich":
            false_item_oak("sandwich")
        elif item_oak == "penny":
            false_item_oak("penny")
        elif item_oak == "bottle":
            false_item_oak("bottle")
        elif item_oak == "baseball":
            false_item_oak("baseball")
        elif item_oak == "used chewing gum":
            false_item_oak("used chewing gum")
        elif item_oak == "hairclip":
            false_item_oak("hairclip")
        else:
            print(f" {item_oak} is not in your bag, please try {bag}.")


def false_item_oak(item):
    print(f"\"Let's try the {item}. Maybe it works.\"")
#    time.sleep(10)
    print("\"Nothing happens, I should try another one.\"")
    print("")
#    time.sleep(5)
    choice_oak()


def search_item_oak():
    if len(random_item_oak) > 0:
        item = random_item_oak.pop(random.randrange(len(random_item_oak)))

        print("You search for other items.")
        print(f"You find a {item}.")
        print("Do you want to put this item in your bag?")

        while True:
            choice = input("> ").lower()

            if choice == "yes":
                bag.append(item)
                print("")
                print(f"The following items are in your bag now: {bag}")
                additional_item_oak()
            elif choice == "no":
                print("ok, I will search something else.")
                search_item_oak()
            else:
                print("yes or no?")
    else:
        print("\"I can't find more items. Let's go back to the oak.\"")
        no_item_works()


def additional_item_oak():
    print("Do you want to search for an additional item or try this one at the oak?")
    while True:
        choice = input("> ").lower()

        if "item" in choice:
            search_item_oak()
        elif "oak" in choice:
            no_item_works()
        else:
            print("item or oak?")


def no_item_works():
    print("")
    print("You go back to the oak.")
    print("While you use to try your new item, you hear the voice again.")
    print("\"It won't work.\"")
    print("\"I will tell you a story about this ancient oak, but first, tell me your name.\"")

    characters.player.name = input("> ")

    time.sleep(3)
    print("")
    print(f"\"{characters.player.name} is a beautyfull name. It's a pleasure to meet... ähmm .. hear you.\"")
    print("\"My name is Vaiana.\"")
    print("\"So let me tell you the story...\"")
    story_oak()


def story_oak():

    print("""
    "Once in the past, there was a time, where humans and nature lived in harmony.
    It was a dependency, important for both sides.
    The nature gave all vital resources to the humans.
    In return, the humans protected the nature from all harm."
    """)
    input("Press Enter to continue...")
    print("""
    "Some people called the nature Gaia, or simply Mother. Others called it holy God.
    But however every nation had another name, they all meaned the same."
    """)
    input("Press Enter to continue...")
    print("""
    "While a small group of people lived close to the nature, they felt its power.
    They learned to put the energy out of their enviromente and to use it for themselves.
    They learned to manipulate the environment by using their minds.
    It was a gift from mother nature!
    """)
    input("Press Enter to continue...")
    print("""
    Where Vaiana's voice sounded really proud before, it changes suddenly into sadness.
    """)
    input("Press Enter to continue...")
    print("""
    "In the same time another nation explored different technologies.
    But instead of using the natures power, they began to destroy everything around them.
    They began to build machines and kill all creatures without a need.
    They lost their connection to the beauty of the nature.
    They began to kill Gaia!"

    ... Vaiana's voice silenced.

    """)
    input("Press Enter to countinue...")

#    time.sleep(5)

    print("""
    "This oak, was a symble of peace between humans and nature. It was the centre of all live."
    The oldest of our village ...."

    """)
    print("Viana's voice is suddenly interupted by a big bang... then there is nothing but silence.")
    print("...")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("You see the birds surrounding the oak, but you can't hear them sing.")
    print("You see the leafs dancing in the wind, but they make no sound.")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("Suddenly a bright light appears. Its center comes direct out of the tree and gets brighter and brighter.")
    print("You have to shut your eyes.")
    print("")
    print("\"What the hell is going on?!!\"")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("You begin to lose your consciousness.")

    health_points.health(-10, characters.player)

    print("The last thing you recognize is Viana`s voice.")
    print("")
    print("\"I'm so sorry! It's not a keyhole, it's a crack in time.\"")
    print("")

    input("Press Enter to countinue...")

    print("")
    time.sleep(5)
    story_wake_up()


def story_wake_up():
    # global hp

    print("")
    print("You wake up and slowly open your eyes.")
    print("You recognize that you lay on the ground.")
    print("The first thing you see is the blue sky and the crown of the tree.")
    print("As you look to the right you can see a person sitting next to you.")
    print("It's a woman, nearly the same age as you are.")
    print("She has long, red hairs and her face is peppered with small freckles.")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("\"Are you ok?\" she asks you and takes your hand.")
    print("\"I'm so sorry, I had no choice!\"")
    print("\"Whh..whhat happend? There was... a light!\"")
    print("\"I will tell you later. We have to leave now.\"")
    print("\"Come on, stand up.\"")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("The woman picks up a leaf of the oak and holds it in both hands.")
    print("A strange green light appears in her hands and surrounds the leaf, only for a few seconds.")
    print("\"Take the leaf and eat it. I know it's not tasty, but it will help you.\" She sais and looks to your forehead.")
    print("In this moment you recognize that blood runs down your face.")
    print("You have a deep cut on your forehead. It must has happend while you lost your consciousness and fell to the ground.")
    print("Carefully, she lays the leaf into your hand and sais with a smile: \"My name is Vaiana. It's a pleasure to meet you.\"")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("Do you want to eat the leaf now or put it in your bag?")
    print(f"Your health points: {characters.player.hp}/{characters.player.hp_max}.")

    while True:
        choice = input("> ").lower()
        if "eat" in choice:
            health_points.health(heal_items.green_leaf.heal, characters.player)
            break
        elif "bag" in choice:
            print("\" Thank you. I will use it later.\"")
            print("You put the leaf in your bag.")
            bag_new.append("green leaf")
            print(f"The following items are in your bag now. {bag_new}")
            break
        else:
            print("eat or bag?")

    leave_oak()


def leave_oak():

    print("")

    input("Press Enter to countinue...")

    print("")
    print("You and Vaiana leave the oak northbound.")
    print("This direction should lead to the school, but there is only a deep wood.")
    print("No streets, no houses, no people.")
    print("Your mind seem to collapse, you are not able to understand what's going on, nore where you are.")
    print("You enter the wood.")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("After walking 2 hours without talking you stop at a clearing.")
    print("\"Let's rest here.\" Vaiana sais.")
    print("\"I know you are confused, I will explain everything later.\"")
    print("\"But now I will show you something helpfull.\"")
    print("\"Do you see the bay tree over there? Go and get a leaf, please.\"")
    print("You get a leaf from the bay tree.")
    print("\"Ok, now hold it in both hands. Close your eyes and think about something that makes you happy.\"")
    print("You follow her instructions, but nothing happens.")
    print("\"Try it again. And now conzentrate on the leaf.\"")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("You close your eyes and think about your family while conzentrating on the leaf.")
    print("Suddenly your whole body feels hot. You can feel how energy flows from the environment straight into your body.")
    print("After a few seconds you open your eyes. The leaf has changed its colour from green to red.")
    print("")

    experience.exp(heal_items.red_leaf.ep)

    print("")

    input("Press Enter to countinue...")

    print("")
    print("\"Wow, what happend?\" You ask.")
    print("Vaiana:\"You transformed Gaias energy and safed it in the leaf.\"")
    print("\"Unbelievable, you are a real natural.\"")
    print("\"Congratulations, you created your first healing-leaf.\"")
    print("\"But why is this one red?\" You want to know.")
    print("\"Yours had a green colour.\"")
    print("Vaiana answers: \"Yes, you are right. It depends on the tree.\"")
    print("\"The red one is stronger, which gives you more health points.\"")
    print("\"Other objects can heal you when you are poisoned or restore your stamina.\"")
    print("\"You can use Gaias power in so many ways.\"")
    print("\"Perplexed you stare into her beautyful braun eyes.\"")
    print("A silent whisper comes out of your mouth: \"Wow, that is so awesome.\"")
    print("")

    print("Do you want to eat the leaf or put it in your bag?")

    while True:
        choice = input("> ").lower()
        if "eat" in choice:
            health_points.health(heal_items.red_leaf.heal, characters.player)
            break
        elif "bag" in choice:
            print("You put the leaf in your bag.")
            bag_new.append("red leaf")
            print(f"The following items are in your bag now. {bag_new}")
            break
        else:
            print("eat or bag?")

    print("")

    input("Press Enter to countinue...")
    pass_dev_land()

def pass_dev_land():

    print("After you packed your things you continue your way towards northeast.")
    print("Vaiana: \"We have to be carefull, we will pass the Devestated Land.\"")
    print("The whole environment was detroyed by the Trolpers. Once there was a deep wood, now it is nothing more than a desert.")
    print("That's why we call it Devestated Land.")
    print("The Trolpers are a nation which developed machines. They began to destroy everything to get more resources.")
    print("Attention! There it is.")
    print("")

    input("Press Enter to countinue...")

    print("")
    print("You look through the trees. You can see a plain full of dead trees. There are no animals, there is nothing but devestation.")
    print("\"This is the Devestated Land.\" You think for yourself. \"Really scary.\"")
    print("\"Hurry up! We have to pass , quick!\" Vaiana says")
    print("You and Vaiana enter the Devestated Land.")
    print("After 200 meters of running Vaiana suddenly push you to the side. You fell into the dust.")
    print("You can hear a loud bang.")
    print("You look to the side. You can see a creature. It looks like a dog but it's not a living thing.")
    print("You look to Vaiana, she seems to be injured, unable to move.")
    print("The creature prepares for an attack. You have to make a decision.")
    print("Grab the branch next to you and fight or flee without Viana?")
    print("")

    while True:
        choice = input("> ").lower()
        if "fight" in choice:
            combat.flee_mode = 1
            weapons.applied_weapon = weapons.branch
            combat.init_fight(2, characters.hellhound)
            hidden_village()
        elif "flee" in choice:
            flee_dev_land()
        else:
            print("fight or flee?")


def flee_dev_land():
    print("You flee in panic. You crash down a hill and lose your consciousness!")
    hidden_village()



def hidden_village():
    time.sleep(10)
    print("")
    print("You open your eyes. You lay in a bed. Don't know what happend to you.")
    

# when flee lose consciousness, wake up later in the hidden village. They tell you the story. Viana and you were rescued.
# when attack, you lose against the enemy and you and vaiana will be rescued. Same story as flee.
# You get a weapon from the resident.


    print("")
    print(">>> to be continued ... <<<")
    print("")
    time.sleep(10)

    exit(0)


pass_dev_land()
