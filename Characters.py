#!/usr/bin/python
from Inventory import Inventory
import random

###############################################################################################################
                                  #----BASE CLASS-----#
###############################################################################################################
class Character:
    '''The Base Character class'''
    def __init__(self, name):
        self.name = name
        self.STATS = {
            'health': 100, #Lowering health should effect all stats except grit and leaderhip
            'maxHealth': 100,
            'strength': 7,
            'dexterity': 7, 
            'wisdom': 7, 
            'constitution': 7,  
            'charisma': 7, 
            'intelligence': 7, 
            'level': 1,
            'xp': 0,
            'ac': 0,
                }
        
        self.EQUIPMENT = {
            'weapon': None,
            'armor': None,
            'shield': None,
                }
        
        self.STATE = {
            'in_Guard': False,
            'in_Action': False,
            'action_determined': False,
            'action_canceled': False,
                }

    def info(self):
        info = ""
        for key in self.STATS:
            info += "{}: {}\n".format(key, self.STATS[key])

        for key in self.EQUIPMENT:
            info += "{}: {}\n".format(key, self.EQUIPMENT[key])
        
        return info

    def armor_class(self):
        if self.STATS['ac'] == 0:
            ac = self.STATS['dexterity'] + self.armor_total()
        else:
            ac = self.STATS['ac'] + self.armor_total()
        return ac
    
    def armor_total(self):
        '''This needs to be modified to take in to account 
            the changes made to self.EQUIPMENT
        '''

        at = 0
        for key in self.EQUIPMENT:
            if self.EQUIPMENT[key] == None:
                continue
            else:
                at += self.EQUIPMENT[key].val
        return at
    
    
    def skillModifier(self, skill):
        modifier = (self.STATS[skill] - 10) / 2
        modifier = round(modifier)
        return modifier


    def attack(self):
        atk = random.randint(1, 6)
        return atk 
##############################################################################################


###############################################################################################
                             #-----PartyMember Class------#
###############################################################################################

class PartyMember(Character):
    def __init__(self, name):
        super().__init__(name)
        self.inventory = Inventory()


    def attack(self):
        if self.EQUIPMENT['weapon'] == None:
            atk = random.randint(1, 6)
        else:
            atk = weapon.attack()

        return atk

    def equip(self, equipment, key):
        if key != equipment.key:
            print("Cannot be equipped to {}".format(key))
            print("key: {}, equipment.key: {}".format(key, equipment.key))
            print("#######################")
            raise Exception
        else:
            self.EQUIPMENT[key] = equipment
    
    def unEquip(self, key):
        self.EQUIPMENT[key] = None
        #This needs some sort of exception handling
        '''
        else:
            print("No such Key as {}".format(key))
            raise Exception
        '''

    def displayArmor(self):
        for key in self.EQUIPMENT:
            print("{}: {}".format(key, self.EQUIPMENT[key]))

    def addStatPoint(self, stat):
        if self.STATS[stat] + 1 <= 20:
            self.STATS[stat] += 1
        	
    def subStatPoint(self, stat):
        if self.STATS[stat] - 1 <= -1:
            #print("You can't go that low")
            self.STATS[stat] = self.stats[stat]
                    
        else:
            self.STATS[stat] -= 1

#################################################################################################


#################################################################################################
                                   #----Enemy Class ------#
#################################################################################################

class Enemy(Character):
    def __init__(self, name):
        super().__init__(name)

        self.SPECIAL_ATTACKS = {
                'SP1': {
                    'cost': None,
                    'atk': None
                    },
                'SP2': {
                    'cost': None,
                    'atk': None
                    },
                'SP3': {
                    'cost': None,
                    'atk': None,
                    },
                }

        self.SKILLS = {
                'link': None,
                'passive': None
                }

        self.stealableItems = []

##################################################################################################


if __name__ == '__main__':
    from Items import ConsumableItem

    


    p = PartyMember('Tika Waylan')
    
    ration = ConsumableItem("Ration", 5, "health")
    kit = ConsumableItem("Healer's Kit", 15, "health")
    ration.quantity = 5
    kit.quantity = 8
    chest = [ration, kit]
    for i in chest:
        p.inventory.addItem(i)
    print("name: {}".format(p.name))
    print("stats: {}".format(p.STATS))
    print("ac: {}".format(p.armor_class()))
    print("inventory: {}".format(p.inventory.info()))
    print()
######################################################
#####################################################
###################################################
    e = Enemy("Black Bear")
    e.STATS['ac'] = 11
    e.STATS['health'] = 30
    e.STATS['strength'] = 15
    e.STATS['dexterity'] = 10
    e.STATS['constitution'] = 14
    e.STATS['intelligence'] = 2
    e.STATS['wisdom'] = 12
    e.STATS['charisma'] = 7
    print("name: {}".format(e.name))
    print("stats: {}".format(e.STATS))

#I'd like the stats to work like fallout. I've done this before.  Like an idiot I'm doing it again haha.
#I think I even made a web version of it LOL.  I suck.  I wouldn't talk to a friend the way I talk to myself....


'''

Formula for skillpoints (Fallout)
Skill_points_per_level = 5 + (2 * Intelligence) Fallout 1/2
skill_points_per_level = 10 + intelligence Fallout 3
Skill_points_per_level = 10 + (intelligence / 2) Fallout New Vegas

Formulas for CTB
COUNTER = TickSpeed * action['rank'] * Haste/Slow['status']

COUNTER = (weapon['speed'] * unit['speed_mod'] + rng(0, 0.5)) * unit['status_mod']



Now, here's a chart relating Agility to Tick Speed:
------------------------+-------------------------+--------------------------
Agi        = Tick Speed | Agi        = Tick Speed | Agi        = Tick Speed
------------------------+-------------------------+--------------------------
170 -  255   = 3        | 19  -  22    = 10       | 4            = 20
------------------------+-------------------------+--------------------------
98  -  169   = 4        | 17  -  18    = 11       | 3            = 22
------------------------+-------------------------+--------------------------
62  -  97    = 5        | 15  -  16    = 12       | 2            = 24
------------------------+-------------------------+--------------------------
44  -  61    = 6        | 12  -  14    = 13       | 1            = 26
------------------------+-------------------------+--------------------------
35  -  43    = 7        | 10  -  11    = 14       | 0            = 28
------------------------+-------------------------+--------------------------
29  -  34    = 8        | 7   -  9     = 15       | *************************
------------------------+-------------------------+--------------------------
23  -  28    = 9        | 5   -  6     = 16       | *************************
------------------------+-------------------------+--------------------------

Formulas for modifers
modifier = (stat['stat_name'] - 10) / 2 #This is legit just the D&D rules

Formula for Fallout Skills
Skill_val = roundUp(2 + (Stat * 2) + [luck / 2])
ex.
Big_Guns = 2 + (5 * 2) + [5 / 2] = 15  

Fallout 3 Skills to steal PLEASE RENAME

Big Guns ==  ?? || Endurance
Energy Weapons ==  ?? || Perception
Explosives == Misslies  || Perception
Repair == Repair        || Inteligence
Science == Research and Development/SkunkWorks? || Intelligence
Small Guns == Small Arms || Agility
Speech == Command || Charisma
Barter == Negotiation || Charisma
Sneak == Tactics || Agility
There should be a defensive one or something


'''

