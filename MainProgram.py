

from FortniteBot import FortniteBot


bot1 = FortniteBot("Chat", 89)
bot2 = FortniteBot("R2-D2", 22)
bot3 = FortniteBot("AM", 1)

bot1.take_damage(5) #does something 
bot2.take_damage(20)

bot1.hunger(+ 5)




print(bot1.health) #holds something
print(bot1.name)

print(bot2.health)
print(bot2.name)

print(bot3.health)
print(bot3.name)

print("Before")
print(bot1.health) #holds something
print(bot2.health)
print(bot3.health)

bot1.max_health = 200

print("After")
print(bot1.health) #holds something
print(bot2.health)
print(bot3.health)