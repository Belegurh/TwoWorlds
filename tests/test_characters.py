import unittest
from TwoWorlds.characters import Characters
import TwoWorlds.experience

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
        # increase health
        self.player.hp = 20
        self.player.hp_max = 40
        self.player.calc_hp(5)
        self.assertEqual(self.player.hp, 25)

        self.hellhound.hp = 20
        self.hellhound.hp_max = 50
        self.hellhound.calc_hp(5)
        self.assertEqual(self.hellhound.hp, 25)

        # decrease health
        self.player.hp = 20
        self.player.hp_max = 40
        self.player.calc_hp(-5)
        self.assertEqual(self.player.hp, 15)

        self.hellhound.hp = 20
        self.hellhound.hp_max = 50
        self.hellhound.calc_hp(-5)
        self.assertEqual(self.hellhound.hp, 15)

        # increase health over hp_max
        self.player.hp = 38
        self.player.hp_max = 40
        self.player.calc_hp(5)
        self.assertEqual(self.player.hp, 40)

        self.hellhound.hp = 48
        self.hellhound.hp_max = 50
        self.hellhound.calc_hp(5)
        self.assertEqual(self.hellhound.hp, 50)

        # decrease health below 0, player dead, exit(0) 
        self.player.hp = 40
        self.player.hp_max = 40           
        self.assertRaises(SystemExit, self.player.calc_hp, -45)

        # decrease health below 0, hellhound dead, change ep and lvl
        self.hellhound.hp = 50
        self.hellhound.hp_max = 50
        self.hellhound.calc_hp(-55)
        self.assertEqual(TwoWorlds.experience.ep_player, 25)
        self.assertEqual(TwoWorlds.experience.lvl_player, 2)


if __name__ == '__main__':
	unittest.main()