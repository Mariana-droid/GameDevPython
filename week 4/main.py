from room import Room
from item import Item
from character import Character
from rpginfo import RPGinfo
from RoomsSetup import *
# Inventory and commands
Inventory = []
commands = ["go","talk","inspect","pick up","use","give","inventory"]

def get_inv():
    print("Here's what you have on you right now:")
    print("|", end="")
    for i in Inventory:
       print(" " + i.get_name() + " |", end="")

def inspect_inv(object):
    for i in Inventory:
        if i.get_name() == object:
            i.describe()
            return
    print("Nothing to inspect here.")

def help():
    print("List of commands available:")
    print("|", end="")
    for command in commands:
        print(" " + command + " |", end="")   


#Moving
current_room = hall
#-------------------------------
#Setting up the begining of the game!

Grinstead_mansion = RPGinfo("Grinstead Mansion")
Grinstead_mansion.welcome()
RPGinfo.info()

print("\nFew things before we get started: This is inspired by old point and click games (think monkey island). So basically collect stuff\n\
combine stuff and use stuff. Got it? Good. These are the commands you can use in the game:")
help()
print("\n\nIf you forget, you can always use the help command to get a reminder. Just, huh, don't forget that one!")

print("There are " + str(Room.number_of_rooms) + " rooms to explore.\n")

while True:
    print("\n")
    current_room.get_details()
    character = current_room.get_character()
    command = input("> ").lower()
    match command:
        #If the player wishes to move
        case "go":
            Answer = input("Which direction would you like to go to?\n> ")
            current_room = current_room.move(Answer)
        #If player wishes to talk to the character    
        case "talk":
            if character is not None:
                character.talk()
            else:
                print("There is no one here to talk to.")
        #case "give":
            
        case "inspect":
            Answer = input("What would you like to inspect?\n> ").lower()
            found = current_room.inspect(Answer)
            if found is False:
                inspect_inv(Answer)
        case "inventory":
            get_inv()
        case "pick up":
            obj_name = input("What would you like to pick up?\n> ").lower()
            object = current_room.pickup(obj_name)
            if object is not None:
                print("You picked up: " + object.get_name() + ".")
                Inventory.append(object)
            else:
                print("You can't pick that up.") 
        case "help":
            help()

        

        
