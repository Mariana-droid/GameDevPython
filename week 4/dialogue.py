class Dialogue():

    def __init__(self, char_name):
        self.name = char_name
        self.options = []
        self.speech = None
        self.answer = None


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
        print("["+ self.name +"]" + self.speech)
        i = 1
        if len(self.options) is 1:
            return self.options[0]
        for option in self.options:
            print("["+str(i)+"] "+ option.get_answer())
            i+=1
        Answer = input("> ")
        if Answer.isdigit() and int(Answer) != 0 and int(Answer) < i:
            if self.options[int(Answer)].get_speech() is None:
                return None 
            return self.options[int(Answer)]
        return self
    