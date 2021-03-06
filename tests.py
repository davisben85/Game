import unittest
from toon import toon, character, mob

class TestPlayer(unittest.TestCase):
	
	def test_player(self):
		health = 100
		block = 60
		attack = 20
		player = character.Character("Ben",attack,block, health)
		self.assertEqual(player.getHealth(),health)
		self.assertEqual(player.getBlock(),block)
		self.assertEqual(player.getAttack(),attack)


class TestMob(unittest.TestCase):

	def test_mob(self):
		health = 20
		block = 50
		attack = 10
		boss = mob.Mob("Boss",attack,block, health)
		self.assertEqual(boss.getHealth(),health)
		self.assertEqual(boss.getBlock(),block)
		self.assertEqual(boss.getAttack(),attack)

if __name__ == '__main__':
	unittest.main()
