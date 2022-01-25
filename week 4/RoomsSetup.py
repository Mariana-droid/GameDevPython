from room import Room
from itemsSetup import *
#Creating the rooms and the descriptions
hall = Room("foyer")
hall.set_description("A large foyer stands before you. You can tell it hasn't been used much. There are a few coats on the hanger,\n\
along with a pair of boots appearing to belong to a young child.")

kitchen = Room("kitchen")
kitchen.set_description("Different kitchen items all lined up, some pans hanging from the ceiling. An old, half chewed loaf\n\
with mold already developed on it, a few flies circling it on a counter. A drawer is also opened, looking very near to falling off to the floor.")

dining_room = Room("dining room")
dining_room.set_description("A vast room with a shiny wooden floor, with a hanging, golden candle chandelier that probably costs more than\n\
you can imagine.In the corner there is a fireplace. The long, mahogany table is set, however the plate sits empty. There is only one.")

hallway = Room("hallway")
hallway.set_description("The absence of windows or light reminds you of a horror movie. Shifting your gaze along the walls,\n\
you can see different old paitings and photos. In the middle, as if blocking your way, stands a small, brown haired woman.")

ballroom = Room("ballroom")
ballroom.set_description("Dust flies in the air as you open the creaking door to go inside. The least visisted room of the house you gather,\
and you understand why as it's only a large, empty space with a smooth, stone floor. However, a little girl stands dancing. A bit stiff\n\
but with a childlike innocence.")

study = Room("study")
study.set_description("It looked like a tornado swarmed it. The desk that sits in front of a window is a mess. Important looking documents\n\
documents lay on the ground. You aren't sure if a fight happened or if someone tried to run. But in the carpet covering the floor you can see it\n\
...\n\
blood.")
study.set_locked(True)

stairs = Room("stairs")
stairs.set_description("A spiral stairways that goes up but also a normal one going down.")

attic = Room("attic")
attic.set_description("Full of boxes. It looks like it has been abandoned for a few years at least. The moonlight coming through the window\n\
gives the room an eerie feeling.")

basement = Room("basement")
basement.set_description("It smells stuffy. It is filled with old, expensive looking furniture. There are a couple broken ones and\n\
some blood specks on the ground")

#Creating the connections
hall.link_room(kitchen,"west")
hall.link_room(hallway,"north")
hall.link_room(dining_room,"east")

kitchen.link_room(hall,"east")

dining_room.link_room(ballroom,"north")
dining_room.link_room(hall,"west")

hallway.link_room(hall,"south")
hallway.link_room(study,"west")
hallway.link_room(ballroom,"east")
hallway.link_room(stairs,"north")

ballroom.link_room(dining_room,"south")
ballroom.link_room(hallway,"west")

study.link_room(hallway,"east")

stairs.link_room(hallway,"south")
stairs.link_room(attic,"up")
stairs.link_room(basement,"down")

attic.link_room(stairs,"down")

basement.link_room(stairs,"up")

#Creating inspecatables in the rooms ^^
hall.inspectable_obj("boots","Picking the boots up, you inspect the soles. They look worn down but also clean,\n\
like they haven't been used in a while.")
hall.inspectable_obj("coats","Albeit relunctely, you start searching the pockets of the coats. You find a few loose change,\n\
house keys and some receipts dating back to 1 month ago. In the last one you find a lighter.")

kitchen.inspectable_obj("bread","You almost throw up getting near it, but persist. After touching it, you move away in fear of it becoming alive.")
kitchen.inspectable_obj("pans","The amount of pans surprises you, as you don't think anyone would ever need to use so many in their lifetime.")
kitchen.inspectable_obj("drawer","Coming closer to the drawer, you see it used to be some sort of tool box. Now however, only a screwdriver remains.")

dining_room.inspectable_obj("chandelier","After using a chair to get higher, you can see upon closer inspection the candles look average enough.")
dining_room.inspectable_obj("fireplace","You look down at the ash covering the opening. Reluctantly, you scavange throught it but find nothing\n\
and unfortunaly it's too dark to look up the chimney.")
dining_room.inspectable_obj("plate","The plate looks porcelain and the silverware is golden. But other than that, nothing special.")

hallway.inspectable_obj("photos","You can an older couple with a woman in her 30s and baby girl. They smile for the picture in front of their house.")
hallway.inspectable_obj("paintings","A painting of the house. It looks newer.")


#Putting objects in rooms
hall.add_inv(lighter)
kitchen.add_inv(screwdriver)
 