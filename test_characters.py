import unittest
from characters import Characters

class TestCharacters(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        self.player = Characters("unknown", 40, 40, 3, 20, 0, "Hand")
        self.hellhound = Characters("Hellhound", 50, 50, 11, 0, 25, "Clow")

    def tearDown(self):
        pass
    
    def test_calc_hp(self):
        self.player.hp = 20
        self.player.calc_hp(5)
        self.assertEqual(self.player.hp, 25)

        self.player.hp = 20
        self.player.calc_hp(-5)
        self.assertEqual(self.player.hp, 15)

        self.player.hp = 40
        self.player.calc_hp(5)
        self.assertEqual(self.player.hp, 40)

        # self.player.hp = 40
        # self.player.calc_hp(-45)
        # self.assertEqual(self.player.hp, 40)


if __name__ == '__main__':
	unittest.main()


#  # calculate hp for all characters
#     def calc_hp(self, change_hp):
#         if ((self.hp + change_hp) <= self.hp_max) and (self.hp + change_hp > 0):
#             self.hp += change_hp
#             if change_hp >= 0:
#                 print(f"hp + {change_hp}, Health points {self.name}: {self.hp}/{self.hp_max}")
#             else:
#                 print(f"hp - {abs(change_hp)}, Health points {self.name}: {self.hp}/{self.hp_max}")
#         elif self.hp + change_hp > self.hp_max:
#             self.hp = self.hp_max
#             print(f"hp + {change_hp}, Health points {self.name}: {self.hp}/{self.hp_max}")
#         elif self.hp + change_hp <= 0:
#             self.hp += change_hp
#             print(f"hp - {abs(change_hp)}")
#             char_dead.dead(self)
#         else:
#             print(">>>failure, wrong hp! Please contact your admin!<<<")