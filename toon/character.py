from toon import Toon

class Character(Toon):
	def __init__(self,name,base_attack,block_chance,base_hp):
		self.xp = 0
		super(Character, self).__init__(name,base_attack,block_chance,base_hp)

	def getXP(self):
		return self.xp

	def setXP(self,earned_xp):
		self.xp += earned_xp


##################


warrior = Character("Ben",50,20,100)
warrior.setXP(10)


print warrior.getName()
print warrior.getStats()
print warrior.getXP()

warrior.setXP(50)

print warrior.getXP()