#!/usr/bin/python

import random
import time
import os  #Need to import some sort of Gui system here.


#######################---COMBAT---#####################################################################
class Combat:
    def __init__(self, list_of_enemies, list_of_partyMembers, gameState):
        self.enemies = list_of_enemies
        self.player_party = list_of_partyMembers
        self.GAMESTATE = gameState
        self.selectable = [] #An empty list to store the indexe of the enemies that can be targeted.
        self._combatents = []   
        self._inv_Phase = inventoryPhase(self.GAMESTATE) 

    def launch(self):
        if type(self.GAMESTATE) == dict and type(self.enemies) == list:
            GS = self.GAMESTATE['COMBAT']
            GS['AMBUSH']['ambushed'] = self.ambushed()
            while GS['in_Combat']:
                if GS['AMBUSH']['determined'] != True and GS['AMBUSH']['ambushed']:
                    print("You've been AMBUSHED!!!")
                    #SOME FUNCTION NEEDS TO GO HERE TO GIVE THE ENEMY PARTY ADVANTAGE 
                    GS['AMBUSH']['determined'] = True
                if GS['determined_Initiative'] != True:
                    for i in self.enemies:
                        self._combatents.append(i)
                    for i in self.player_party:
                        self._combatents.append(i)
                    self._combatents = self.determineInitiative(self._combatents) 
                    GS['determined_Initiative'] = True
               
                while GS['in_Combat']: # This actually needs to be a check for the enemy parties hp and the Player parties HP.
                    self.displayTurnOrder()
                    for i in self._combatents:
                        if type(i) == Enemy:  
                            ''' This is where the enemy action is determined.'''
                            os.system('clear')
                            dmg = i.attack()
                            sel = random.randint(1, len(self.player_party))#This could be better but is fine for right now.
                            #print("sel: {}".format(sel)) #use this to verify party member selection
                            target = self.player_party[sel - 1]
                            if target.STATE['in_Guard']:
                                dmg = (dmg / 2)
                                dmg = round(dmg)
                            target.STATS['health'] -=dmg
                            print("{} does {} dmg to {}".format(i.name, dmg, target.name))
                            time.sleep(1)
                        else:
                            partyMember = i
                            while partyMember.STATE['action_determined'] != True:
                                partyMember.STATE['action_canceled'] = False
                                os.system('clear')
                                print("{}'s health: {}".format(partyMember.name, partyMember.STATS['health']))
                                print("Select in Action.")
                                print("G: Guard, A: Attack, I: Use Item, C: Change Equipment, Q: Quit")
                                selection = input(">?")

                                if selection in ["G", "g"]:
                                    os.system('clear')
                                    print("{}'s Guard stance activated".format(partyMember.name))
                                    partyMember.STATE['in_Guard'] = True
                                    time.sleep(1)
                                    continue 
                            
                                elif selection in ["A", "a"]:  
                                    
                                    #This whole branch should be put into it's own function with error handling
                                    
                                    while partyMember.STATE['action_canceled'] != True:
                                        print("Who to attack?")
                                        self.listEnemies()
                                        print("C: Cancel")
                                        selection = input(">?")
                                    
                                        try:
                                            if selection in self.selectable:
                                                target = self.enemies[int(selection)]
                                                dmg = i.attack()
                                                target.STATS['health'] -= dmg
                                                os.system('clear')
                                                print("{} hit the {} for {} damage".format(i.name, target.name, dmg))
                                                print("Enemy {}'s health: {}".format(target.name, target.STATS['health']))
                                                time.sleep(2)
                                                GS['in_Combat'] = False
                                                i.STATE['action_determined'] = True
                                                #break
                                            else:
                                                if selection in ["C", "c"]:
                                                    partyMember.STATE['action_canceled'] = True
                                                
                                                
                                        except ValueError:
                                            os.system('clear')
                                            print("That is not a valid selection")
                                        
                                        #return partyMember.STATE['action_determined']  
                                #elif selection in ["I", "i"]:


                                elif selection in ["Q", "q"]:
                                    GS['in_Combat'] = False
                                    break
                                else:
                                    os.system('clear')
                                    print("That is not a valid selection")
                                    time.sleep(1)

                    self.clearSelectable()
        else:
            raise Exception

    def listEnemies(self):
        counter = 0
        for e in self.enemies:
            print("{} for {}\n".format(counter, e.name))
            self.selectable.append(str(counter))
            counter += 1

        for c in self.player_party:
            print("{} for {}\n".format(counter, c.name))
            self.selectable.append(str(counter))
            counter += 1
        
        time.sleep(1) 
    
    
    def clearSelectable(self): #Does this need to be outside this function?
        self.selectable = []
    
    def ambushed(self):
        r_Ambushed = False
        roll = random.randint(1,10)
        if roll < 4:
            r_Ambushed = True

        return r_Ambushed


    def determineInitiative(self, combatent_list):
        '''Is there a way for this not to return a tuple? It's too confusing when you 
            read the code later.  However it's nice to see the previous roll because
            it helps you to know that your code is working.  I don't know.
            as of right now it's returning a list with only the combatnets. It doesn't 
            reference their initiative numbers at all.  
        '''
        def unitsRoll(e):
                return e[1]
        turn_order_list = [] 
        roll_list = []
        prev_rolls = []
        for combatent in combatent_list:
            flag = False
            modifier = combatent.skillModifier('dexterity')
            while flag != True:
                roll = random.randint(1,20) + modifier
                if roll in prev_rolls:
                    #roll = random.randint(1,20)
                    continue
                else:
                    t = (combatent, roll)
                    roll_list.append(t)
                    prev_rolls.append(roll)
                    flag = True
        roll_list.sort(reverse=True, key=unitsRoll)
        for i in roll_list:
            turn_order_list.append(i[0])
        return turn_order_list

    def displayTurnOrder(self):
        for i in self._combatents:
            print(i.name)
        time.sleep(1)


    

########################################################################################################

########################################################################################################

class inventoryPhase:
    def __init__(self,  gameState):
         
        self.GAMESTATE = gameState
        self.selItem = []
    
    
    def launch(self, inventory):
        if type(self.GAMESTATE) == dict:
            GS = self.GAMESTATE
            GS['INVENTORY']['in_Inventory'] = True
        while GS['INVENTORY']['in_Inventory']:
            if GS['COMBAT']['in_Combat']:
                print("What Item would you like to use?")
                for n, i in enumerate(inventory):
                    print("{} for {}".format(n, i.__str__()))
                    self.selItem.append(str(n))
                print("X: exit")

                selection = input(">?")
                if selection in self.selItem:
                    if isinstance(inventory[int(selection)], Weapon):
                        print("you can't use that")
        
                    else:
                        print("You just used {}".format(inventory[int(selection)].name))
                        GS['INVENTORY']['in_Inventory'] = False 
                elif selection in ["X", "x"]:
                    GS['INVENTORY']['in_Inventory'] = False
        
        

                else:
                    os.system('clear')
                    print("That's not a valid selection")

            self.selItem = []



if __name__ == "__main__":
    from Characters import PartyMember, Enemy
    from Settings import GAMESTATE 


    p1 = PartyMember('Wilhelm Lock')
    #p2 = PartyMember('Tyka Evenstar')
    party = [p1]
    e = [Enemy('Rat'), Enemy('Boar'), Enemy('Lion')]
    g = GAMESTATE
    g['COMBAT']['in_Combat'] = True
    c = Combat(e, party,  g)
    #i = inventoryPhase(c.GAMESTATE)
    print(c.GAMESTATE)
    print(c._inv_Phase.GAMESTATE)
    #print(i.GAMESTATE)
    g['COMBAT']['in_Combat'] = False
    print(c.GAMESTATE)
    #print(i.GAMESTATE)
    #c.launch()

