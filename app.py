from toon import toon, character,mob

warrior = character.Character("Ben",50,20,100)
warrior.setXP(10)
boss = mob.Mob("Boo",20,20,20)

print warrior.getName()
print warrior.getStats()
print warrior.getXP()

warrior.setXP(50)

print warrior.getXP()
print boss.getName()
print boss.getStats()