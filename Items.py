import random

class Item:
    def __init__(self, name):
        self.name = name
        self.cost = 1
        self.weight = 1
        self.quantity = 1
        self.maxQuantity = 10

    def __str__(self):
        x = "{}({})".format(self.name, self.quantity)
        return x




    def reduceQuantity(self):
        self.quantity -= 1
        if self.quantity <= 0:
            del self #This doesn't work.  How can I get rid of the Item object from Memory when it's quantity == 0?


class ConsumableItem(Item):  #Using this as the bases for healing items for right now
    def __init__(self, name, val, stat):
        super().__init__(name)
        self.val = val 
        self.stat = stat
    
    def use(self, target):
        target.stats[self.stat] += self.val
        self.reduceQuantity()        
    
        
class Weapon(Item):
    def __init__(self, name, num_of_rng, range_of_rng):
        super().__init__(name)
        self.equipped = False
        self.damage = None
        self.num_of_rng = num_of_rng
        self.range_of_rng = range_of_rng
        self.damage_type = None
        self.two_handed = False
        self.type = None
        self.family = None
        self.ammunition = None
        self.mod = None #This could be a list so that you could have some weapons that benefit from multiple modifiers?
    
    def attack(self):
        atk = 0
        for i in range(self.num_of_rng):
            roll = random.randint(1, self.range_of_rng)
            atk += roll

        return atk

    def __str__(self):
        return "{}".format(self.name)
        
    
class Ammunition(Weapon):
    def __init__(self):
        super.__init__()

        self.type = str()

    def __str__(self):
        return "I'm ammo for a vulcan cannon"



if __name__ == '__main__':
    from Characters import PartyMember
    
    p = PartyMember("Kodak Black")
    healthItem = ConsumableItem("Healer's Kit", 15, "health")
    p.stats['health'] = 55
    print(p.info())
    healthItem.use(p)
    print(p.info())
    print(healthItem)
    w = Weapon("Sickle", 1, 4)
    print("{}: attacks for {} damage.".format(w.name, w.attack()))





