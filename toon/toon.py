# Default toon object

class Toon(object,base_hp,base_attack,block_chance):
	def __init__(self):
		self.hp = base_hp
		self.attack = base_attack
		self.block = block_chance

	def attack_weight(self,level):
		attack = self.attack * ( self.level * .25 )

	def defense_weight(self,level):
		defense = self.block * ( self.level * .10 )

	def move(self,speed):
		distance = self.speed
