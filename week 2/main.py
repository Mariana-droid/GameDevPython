from room import Room
from item import Item

#Creating items
sword = Item("Sword")

#Creating the rooms
kitchen = Room("kitchen")
kitchen.set_description("A dank and dirty room with flies")


ballroom = Room("ballroom")
ballroom.set_description("A large room with ornate golden decorations on each wall")

dining_hall = Room("dining hall")
dining_hall.set_description("A vast room with a shiny wooden floor; huge candlesticks guard the entrance")

#Linking rooms
dining_hall.link_room(ballroom,"West")
dining_hall.link_room(kitchen,"North")

ballroom.link_room(dining_hall,"East")

kitchen.link_room(dining_hall,"South")

#Moving
current_room = kitchen

while True:
    print("\n")
    current_room.get_details()
    command = input("> ")
    current_room = current_room.move(command)
