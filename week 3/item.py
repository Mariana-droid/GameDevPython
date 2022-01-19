class Item():

    def __init__(self, item_name):
        self.name = item_name
        self.description = None

    #setters
    def set_name(self,item_name):
        self.name = item_name
    def set_description(self,description):
        self.description = description
    
    #getters
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    
    #Get the description
    def describe(self):
        print(self.description)

    #Get the description for the when it's in a room
    def room(self):
        print("There is a " + self.name + " in this room.")
