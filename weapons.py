# currently equipped weapon
applied_weapon = "hand"
weapon_enemy_1 = "hand"

# class weapons
class Weapons:

    # init-method
    def __init__(self, name, weight, demage):
        self.name = name
        self.weight = weight
        self.demage = demage

# instances
branch = Weapons("Branch", 2.4, -3)
claw = Weapons("Claw", 2.4, -4)
