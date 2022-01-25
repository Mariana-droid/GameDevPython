from room import Room
from item import Item
from character import Enemy, Friend
from rpginfo import RPGinfo
from RoomsSetup import *
#
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

#Creating the enemy
Dave = Enemy("Dave","He is a decomposing corpse.")
Dave.set_conversation("*inhuman grunts*")
Dave.set_weakness("stake")

#Creating the friend
Joana = Friend("Joana","She is a small, brown-haired woman with a frown on her face.")
Joana.set_conversation("I don't wanna talk. I'm so hungry.")
Joana.set_afterGift("Thank you again for the food.")
Joana.set_favGift("apple")
Joana.set_inventory("sword")

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
    if character is not None:
        character.describe()
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
        #if the player wants to fight the character
        case "fight":
            if isinstance(character,Enemy):
                item = input("What would you wish to fight " + character.get_name() + " with?\n> ").lower()
                Answer = character.fight(item)
                if Answer is False:
                    exit()
                current_room.set_character(None)
            elif isinstance(character,Friend):
                print("You can't fight " + character.get_name() + ".")
            else:
                print("There no one here to fight.")
        case "give":
            if isinstance(character,Friend):
                gift = input("What would you like to give " + character.get_name() + "?\n> ").lower()
                Answer = character.gift(gift)
                if Answer is True:
                    print("You got a " + character.get_inventory() + ".")
            elif isinstance(character,Enemy):
                print("You can't give stuff to an enemy.")
            else:
                print("No one here to give things to.")

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

        

        
