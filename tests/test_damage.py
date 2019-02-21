import unittest
import TwoWorlds.damage
import TwoWorlds.characters
import TwoWorlds.weapons

class TestDamage(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        pass

    @classmethod
    def tearDownClass(cls):
        pass

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def test_rnd_dmg(self):
        TwoWorlds.characters.player.strength = -1
        TwoWorlds.weapons.branch.damage = -1
        self.assertEqual(TwoWorlds.damage.rnd_dmg(TwoWorlds.characters.player, TwoWorlds.weapons.branch), 0)


if __name__ == '__main__':
    unittest.main()