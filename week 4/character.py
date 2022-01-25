class Character():

    # Create a character
    def __init__(self, char_name, char_description):
        self.name = char_name
        self.conversation = None

    def get_name(self):
        return self.name
    
    def set_name(self,name):
        self.name = name


    # Set what this character will say when talked to
    def set_conversation(self, conversation):
        self.conversation = conversation

    # Talk to this character
    def talk(self):
        if self.conversation is not None:
            print("[" + self.name + " says]: " + self.conversation)
        else:
            print(self.name + " doesn't want to talk to you")

