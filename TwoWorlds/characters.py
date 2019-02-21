import TwoWorlds.char_dead

class Characters(object):

    def __init__(self, name, hp, hp_max, strength, concentration, ep, weapon):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.strength = strength
        self.concentration = concentration
        self. ep = ep
        self. weapon = weapon


    # calculate hp for all characters
    def calc_hp(self, change_hp):
        if ((self.hp + change_hp) <= self.hp_max) and (self.hp + change_hp > 0):
            self.hp += change_hp
            if change_hp >= 0:
                print(f"hp + {change_hp}, Health points {self.name}: {self.hp}/{self.hp_max}")
            else:
                print(f"hp - {abs(change_hp)}, Health points {self.name}: {self.hp}/{self.hp_max}")
        elif self.hp + change_hp > self.hp_max:
            self.hp = self.hp_max
            print(f"hp + {change_hp}, Health points {self.name}: {self.hp}/{self.hp_max}")
        elif self.hp + change_hp <= 0:
            self.hp += change_hp
            print(f"hp - {abs(change_hp)}")
            TwoWorlds.char_dead.dead(self)
        else:
            print(">>>failure, wrong hp! Please contact your admin!<<<")



player = Characters("unknown", 40, 40, 3, 20, 0, "Hand")
hellhound = Characters("Hellhound", 50, 50, 11, 0, 25, "Clow")