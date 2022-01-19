class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.description = char_description
        self.conversation = None

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name


    # Describe this character
    def describe(self):
        print( self.name + " is here!" )
        print( self.description )

    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

    # Fight with this character
    def fight(self, combat_item):
        print(self.name + " doesn't want to fight with you")
        return True

class Enemy(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name, char_description)
        self.weakness = None

    def set_weakness(self,weakness):
        self.weakness = weakness
    
    def get_weakness(self):
        return self.weakness
    
    def fight(self, combat_item):
        if combat_item == self.weakness:
            print("You fend " + self.name + " off with the "+ combat_item + ".")
            return True
        else:
            print(self.name + " crushes you. Yikes.")
            return False

class Friend(Character):

    def __init__(self, char_name, char_description):
        super().__init__(char_name,char_description)
        self.inventory = None
        self.favGift = None
        self.afterGift = None

    #Setters
    def set_inventory(self,inventory):
        self.inventory = inventory
    def set_favGift(self,gift):
        self.favGift = gift
    def set_afterGift(self,speech):
        self.afterGift = speech

    #Getters
    def get_inventory(self):
        return self.inventory
    def get_favGift(self):
        return self.favGift

    def gift(self,gift):
        if gift == self.favGift:
            print("[" + self.name + " says]: " + "This is just what I needed! Thanks.")
            self.conversation = self.afterGift
            return True
        else:
            print("[" + self.name + " says]: " + "I don't need this right now.")
            return False
    
    
