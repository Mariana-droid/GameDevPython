class Character():

    # Create a character
    def __init__(self, char_name):
        self.name = char_name
        self.conversation = None

    def get_name(self):
        return self.name
    def get_conversatition(self):
        return self.conversation
    
    def set_name(self,name):
        self.name = name
    def set_conversation(self,conversation):
        self.conversation = conversation 

    # Talk to this character
    def talk(self):
        Temp = self.conversation #Temporary object of dialogue my god this english is awful
        while (1):
            Temp = Temp.action()
            if Temp is None:
                break