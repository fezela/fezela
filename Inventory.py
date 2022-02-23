#!/usr/bin/python

class Inventory(list):
    def __init__(self):
        self.maxSize = 15
    

    def isInInventory(self, item):
        inInventory = False
        for i in range(len(self)):
            if self[i].name == item.name:
                inIventory = True
            

        return inIventory

    
    def addItem(self, item):
        
        if len(self) == 0:
            self.append(item)
        else:
            for i in range(len(self)):
                if item.name == self[i].name:
                    if (self[i].quantity + item.quantity) >= self[i].maxQuantity:
                        self[i].quantity = self[i].maxQuantity
                    else:
                        self[i].quantity += item.quantity
                    del item #removes unnecessary item objects from memory
        
                else:
                    if (len(self) + 2 < self.maxSize):
                        self.append(item)

                    else:
                        print("ERROR not enough space in inventory")

    def clean(self):
        for i in range(len(self)):
            if self[i].quantity <= 0:
                item = self.pop(i)
                del item



    def info(self):
        '''Use this if you want to see the user representation of the contents of the inventory
            use  __str__() or simply print(inventory_name) to see the Objects and their memory 
            locations.
        '''
        if len(self) != 0:
            x = "["
            for i in range(len(self)):
                x += self[i].__str__()
            
                if (i + 1) != len(self):
                    x += ", "
            x += "]"
            return x

        else:
            return self.__str__()


if __name__ == '__main__':
    from Items import Item

    item = Item("Healer's Kit")
    item2 = Item("Sling")
    INV = Inventory()
    print(INV.info())
    for i in range(20):
        INV.addItem(item)
    
    INV.addItem(item2)
    print(INV.info())
    item2.quantity = 0
    print(INV.info())
    INV.clean()
    print(INV)
    print(INV.info())
    print(len(INV))
