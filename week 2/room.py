class Room():

    def __init__(self, room_name):
        self.name = room_name
        self.description = None
        self.linked_rooms = {}

    #Setters
    def set_name(self,name):
        self.name = name
    def set_description(self,room_description):
        self.description = room_description

    #Getters
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description

    #Print description    
    def describe(self):
        print(self.description)

    #Link the rooms (only goes one way)
    def link_room(self,room_to_link,direction):
        self.linked_rooms[direction] = room_to_link
        #print(self.name + " linked rooms:" + repr(self.linked_rooms))
    
    #Get all details about the room
    def get_details(self):
        print("You are in the " + self.get_name())
        self.describe()
        print("-------------------")
        for direction in self.linked_rooms:
            room = self.linked_rooms[direction]
            print ("The "+ room.get_name() + " is "+ direction)

    #move
    def move(self,direction):
        if direction in self.linked_rooms:
            return self.linked_rooms[direction]
        else:
            print("You can't go that way")
            return self