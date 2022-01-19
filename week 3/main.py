from room import Room
from item import Item
from character import Enemy, Friend

#Creating items
stake = Item("stake")
stake.set_description("A small wooden stake. It appears quite sharp.")

#Creating the rooms
kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room with flies")
kitchen.set_inventory(stake)


ballroom = Room("ballroom")
ballroom.set_description("A large room with ornate golden decorations on each wall")

dining_hall = Room("dining hall")
dining_hall.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

#Linking rooms
dining_hall.link_room(ballroom,"west")
dining_hall.link_room(kitchen,"north")

ballroom.link_room(dining_hall,"east")

kitchen.link_room(dining_hall,"south")

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
current_room = kitchen
kitchen.set_character(Joana)
dining_hall.set_character(Dave)

while True:
    print("\n")
    current_room.get_details()
    character = current_room.get_character()
    if character is not None:
        character.describe()
    command = input("> ")
    #If the player wishes to move
    match command:
        case "go":
            Answer = input("Which direction would you like to go to?\n")
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
                item = input("What would you wish to fight " + character.get_name() + " with?\n>")
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
                gift = input("What would you like to give " + character.get_name() + "?\n")
                Answer = character.gift(gift)
                if Answer is True:
                    print("You got a " + character.get_inventory() + ".")
            elif isinstance(character,Enemy):
                print("You can't give stuff to an enemy.")
            else:
                print("No one here to give things to.")
        

        
