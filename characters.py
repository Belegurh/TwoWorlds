
class Characters:

    def __init__(self, name, hp, hp_max, strength, conzentration, ep, weapon):
        self.name = name
        self.hp = hp
        self.hp_max = hp_max
        self.strength = strength
        self.conzentration = conzentration
        self. ep = ep
        self. weapon = weapon



# good characters
player = Characters("unknown", 40, 40, 3, 20, 0, "Hand")

# close-combat enemies
hellhound = Characters("Hellhound", 50, 50, 11, 0, 25, "Clow")

# range-combat enemies
