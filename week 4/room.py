
from item import Item
class Room():
    
    number_of_rooms = 0

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}
        self.inspectable = {}
        self.character = None
        self.inventory = []
        self.locked = False
        Room.number_of_rooms += 1

    #Setters
    def set_name(self,name):
        self.name = name
    def set_description(self,room_description):
        self.description = room_description
    def set_character(self,character):
        self.character = character
    def set_inventory(self,inventory):
        self.inventory = inventory
    def set_locked(self,lock):
        self.locked = lock

    #Getters
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_character(self):
        return self.character
    def get_inventory(self):
        return self.inventory
    def get_locked(self):
        return self.locked

    #add to inventory
    def add_inv(self,object):
        self.inventory.append(object)

    #Print description    
    def describe(self):
        print(self.description)

    #Link the rooms (only goes one way)
    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction] = room_to_link
        
    #Add inspecatble object
    def inspectable_obj(self,object,description):
        self.inspectable[object] = description


    #Get all details about the room
    def get_details(self):
        print("You are in the " + self.get_name())
        self.describe()
        print("-------------------")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print ("The "+ room.get_name() + " is "+ direction)
        print("-------------------")

    #When interacting with object
    def inspect(self,object):
        if object in self.inspectable:
            print(self.inspectable[object])
            return True
        else:
            return False
            
    #move
    def move(self,direction):
        if direction in self.linked_rooms:
            if self.linked_rooms[direction].get_locked() == False:
                return self.linked_rooms[direction]
            print("It appears to be locked.")
            return self
        else:
            print("You can't go that way.")
            return self
    
    #Pickup Object
    def pickup(self,object_name):
        for object in self.inventory:
            if object.get_name() == object_name:
                if object.get_pickable() is True:
                    self.inventory.remove(object)
                    return object
        return None