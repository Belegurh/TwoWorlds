# heal_items class (Make a class with the name heal_item)
class heal_items:

    # class-variables
    heal_boni = 1.2      # depending on mind_lvl, heal-points can be increased (in %)

    # init-method (class heal_item has-a init that takes self, heal, .. parameters)
    def __init__(self, heal, weight, costs, ep, concentration, ingredient_list):
        self.heal = heal
        self.weight = weight
        self.costs = costs
        self.ep = ep
        self.concentration = concentration      # concentration == mana
        self.ingredient_list = ingredient_list

# instances
green_leaf = heal_items(10, 0.1, 12, 10, 20, ["leaf_oak"])
red_leaf = heal_items(20, 0.1, 15, 12, 30, ["leaf_bay"])
yellow_leaf = heal_items(30, 0.1, 20, 15, 50, ["leaf_oak", "leaf_bay"])
