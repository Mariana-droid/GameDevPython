from colors import style

class RPGinfo():
    def __init__(self, game_title):
        self.title = game_title
    
    def welcome(self):
        #print("\033[91m{}\033[00m".format("Welcome to " + self.title))
        #print(style.RED + "Welcome to " + self.title + style.RESET);
        print("Welcome to " + self.title)

    @staticmethod
    def info():
        print("Made using the OOP RPG game create (c) Curious-droid")
