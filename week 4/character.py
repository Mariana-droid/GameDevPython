class Character():

    # Create a character
    def __init__(self, char_name):
        self.name = char_name
        self.conversation = None
        self.firstConversation = None
        self.firstTime = True

    def get_name(self):
        return self.name
    def get_conversatition(self):
        return self.conversation
    def get_firstConversatition(self):
        return self.firstConversation
    
    def set_name(self,name):
        self.name = name
    def set_conversation(self,conversation):
        self.conversation = conversation 
    def set_firstConversation(self,conversation):
        self.firstConversation = conversation

    # Talk to this character
    def talk(self):
        if self.firstTime:
            Temp = self.firstConversation #If it's the first conversatition
        else:
            Temp = self.conversation #Temporary object of dialogue my god this english is awful
        self.firstTime = False
        while (1):
            Temp = Temp.action()
            if Temp is None:
                break