# Default toon object

class Toon(object):

	def __init__(self,name,base_attack,block_chance,base_hp):
		self.hp = base_hp
		self.attack = base_attack
		self.block = block_chance
		self.name = name

	def getName(self):
		return self.name

	def attack_weight(self,level):
		attack = self.attack * ( self.level * .25 )

	def defense_weight(self,level):
		defense = self.block * ( self.level * .10 )

	def move(self,speed):
		distance = self.speed

	def inventory(self,items):
		current_inventory = self.items

	def takeDamage(self,damage):
		self.hp -= damage

	def restoreHealth(self,heal):
		self.hp += heal

	def isDead(self, hp):
	    if(self.hp <= 0):
	    	return True

	def getStats(self):
		stats = []
		stats.append("Attack:%d" % self.attack)
		stats.append("Block:%d" % self.block)
		stats.append("Health:%d" % self.hp)
		return stats