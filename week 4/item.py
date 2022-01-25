class Item():

    def __init__(self, item_name):
        self.name = item_name
        self.description = None
        self.pickable = True

    #setters
    def set_name(self,item_name):
        self.name = item_name
    def set_description(self,description):
        self.description = description
    def set_pickable(self,pickable):
        self.pickable = pickable
    
    #getters
    def get_name(self):
        return self.name
    def get_description(self):
        return self.description
    def get_pickable(self):
        return self.pickable
    
    #Get the description
    def describe(self):
        print(self.description)

    
