class FortniteBot:
   
    max_health = 100 #Class level variable, effects all bots
   
   
    def __init__(self, bot_name, start_position): #constructor - Run's once when created
        self.name = bot_name #attribute
        self.health = 100  #attribute


    def take_damage(self, amount): #method
        self.health -= amount

    def hunger(self, amount)
            self.hunger_level = 100
            self.hunger_level += amount
            self.hunger_level -= amount
