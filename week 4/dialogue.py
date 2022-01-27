class Dialogue():

    def __init__(self, char_name):
        self.name = char_name
        self.options = [] #options after speech
        self.speech = None #What the character says
        self.answer = None #The answer it displays that leads to the speech


    def get_name(self):
        return self.name
    def get_speech(self):
        return self.speech
    def get_answer(self):
        return self.answer


    def set_name(self,name):
        self.name = name
    def set_speech(self,speech):
        self.speech = speech
    def set_answer(self,answer):
        self.answer = answer

    
    def add_option(self,option):
        self.options.append(option)
    
    def action(self):
        print("["+ self.name +"] " + self.speech) #Saying the character phrase
        i = 1
        if len(self.options) ==1: # If there is only one option, use it (usually only to go back to the first speech)
            return self.options[0]
        for option in self.options: # setting up possible answers
            print("["+str(i)+"] "+ option.get_answer())
            i+=1
        Answer = input("> ") #Ask for answer 
        if Answer.isdigit() and int(Answer) != 0 and int(Answer) < i: #if it's not a digit and it's not within the range of options then send yourself back
            Answer = int(Answer)
            Answer = Answer-1
            if self.options[Answer].get_speech() is None: #If there is no speech after option then exit dialogue
                return None 
            return self.options[Answer] 
        return self
    