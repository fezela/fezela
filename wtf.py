#!/bin/python3

from Items import Item
"""
Actions:

Both players and enemies can use actions.
Actions open subcommands or actions?

Example

Attack
Defend
Cast
    -spell1
    -spell2
    -etc
Special Attack
    -specAtk1
    -etc
Use
    -(opens Item Selection Window)


Concept

Action
    -properties
        -name
        -type //melee||ranged //is this necessary? Maybe if the damage is calculated differently for each
        -rank //determines the attack speed
    -methods
        -effect

I don't think the above is correct because I don't think the Actions should calculate effects.
EX.

Attack does damage but does the attack option need to actually asssess the damage dealt out? Yea, one is interface/view the other is the controller of the model.

I think attack should simply determine the damage output. Or maybe it should just apply effing damage dude!
"""

'''
In FFX they had something I though was really cool, basically the game showed you the move order in a 
little turn window.  Different attacks and spells would effect this turn order actively throughout the 
battle.  Really it's probably how the Active Time Battle system worked throughout the Final Fantasy
series but this was the first time that I think you ever got to actually see how you decesicions 
effected the turn order.  I think sometimes RPG fights feel a little random.  I just always really
liked that touch, because it added another layer of strategy to the game.  I don't really know if 
it made it easier or what but I always really liked that touch.

Having done some brief reading on the subject it appears that move order was affected by agility, and
ability ranks.  Ability were ranked in 3 catagories.  1 being the fastest and 3 being the slowest.  
Agility affected your chance of being the first to attack.  However then your agility withen ranges 
was what gave you what is unofficially called your 'tick counter'  the lower this counter the more
chances you had to attack during a battle.  Those catagories of attacks I refered to early also 
affected the tick counter as well as spells like haste and slow.

EX.

Changing Equipment  === Rank 1 (fastest) action//Maybe no penalty, IDK?
Item use and certain character actions === Rank 2 
Most other actions === Rank 3
Agility works withen ranges.  i.e. agility between 20 and 27 equals the same tick value
Agility advantage maxed out at 170 for first turn advantage.  Your tick value could get no lower.
THe spell Haste lowered your tick value by half.
The spell Slow increased your tick value by 50%.
'''



class Option:
    ''' The base Action Class'''
    def __init__(self, name):
        self.name = name

    def effect(self):
        """The primary means for utilizing an action
            effect takes whatever information is necessary
            and applies it to the user/target/both/other
        """
        x = "Don't instantiate the base class!"
        print(x)
        return x

class Attack(Option):
    '''The Attack action is used to determine the base damage output of the attacker.'''
    def __init__(self, attacker, name="Attack"):
            super().__init__(name)
            self.attacker = None
            self.target = None
            

    def effect(self):
        """Returns the baseDmg of the Attack
            ."""
        
        dmg = self.attacker.strength
        #print("{} attacks {} for {} damage", self.attacker.name, self.target.name, dmg) 
        #self.target.health -= dmg
        return dmg

class Weapon:
    def __init__(self, name):
        self.name = name

    def attack(self, target):
        if type(target) == list:
            print("Multiple targets")

        else:
            print("Single Target")

class Sword(Weapon):
    def __init__(self, name):
        super().__init__(name)
        self.strength = None
        self.equipped = False
        self.cost = 0


class Armor:
    def __init__(self, name, bodySection):
        self.name = name
        self.bodySection = None
        self.val = 0

    def equip(self, player, body_part):

        body_part = self
    
        


            



def inventoryPhase(inventory):
    inInventory = True
    selItem = []
    while inInventory:
        print("What Item would you like to use?")
        for n, i in enumerate(inventory):
            print("{} for {}".format(n, i.name))
            selItem.append(str(n))
        print("X: exit")

        selection = input(">?")
        if selection in selItem:
            if isinstance(inventory[int(selection)], Weapon):
                print("you can't use that")
        
            else:
                print("You just used {}".format(inventory[int(selection)].name))
           
        elif selection in ["X", "x"]:
            inInventory = False
        
        

        else:
            os.system('clear')
            print("That's not a valid selection")

        selItem = []


def equipPhase(equipment):
    selItem = []
    print("What would you like to Do?")
    print("E: Equip Armor or Weapon, U: Unequip Armor or Weapon, X: exit")
    selection = input(">?")
    if selection in ["C", "c"]:
        for n, e in enumerate(equipment):
            print("{} for {}".format(n, e.name))
            selItem.append(str(n))
             
    selection = input(">?")
    if selection in selItem:
        if isinstance(inventory[int(selection)], Weapon):
            print("you can't use that")
        
        else:
            print("You just used {}".format(inventory[int(selection)].name))
           
    else:
        print("That's not a valid selection")

    selItem = []


if __name__ == "__main__":
    import os
    import time #only for testing purposes
    from Characters import PartyMember
    from Phases import Combat
    from Settings import GAMESTATE
    player = PartyMember(name='Thsyn Wingnut')
    bread, ginger, water, mint = Item('Bread'),  Item('Ginger'), Item('Water'), Item('Mint')
    GAMESTATE['started'] = True
    enemies = ['rat','spider','wolf']
    
    inventory = [bread, ginger, water, mint]
    while GAMESTATE['started']:
        os.system("clear")
        print("A: Attack, I: Item Inventory, E: Equipment Inventory, Q: Quit\n" )
        options = input(">?")
        if options in ['A', 'a']:
            os.system('clear')
            GAMESTATE['COMBAT']['in_Combat'] = True
            combat = Combat(enemies, player, GAMESTATE)
            combat.launch()
            del combat 
            
        
        elif options in ['I', 'i']:
            os.system('clear')
            inventoryPhase(inventory) 
        
        elif options in ['E', 'e']:
            os.system('clear')
            print("Build Equipment Phase function")
            time.sleep(2)
        
        elif options in ['Q','q']:
            print("exiting now")
            
            break
            

        else:
            print("That is not an option")
            continue
