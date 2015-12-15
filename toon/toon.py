# Default toon object

class Toon(object,base_hp,base_attack,block_chance):
	def __init__(self):
		self.hp = base_hp
		self.attack = base_attack
		self.block = block_chance

	def attack_weight(self):
		return self.attack

	def defend(self):
		return self

	def move(self): 
