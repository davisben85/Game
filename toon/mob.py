from toon import Toon
class Mob(Toon):
	def __init__(self,name,base_attack,block_chance,base_hp):
		super(Mob, self).__init__(name,base_attack,block_chance,base_hp)
