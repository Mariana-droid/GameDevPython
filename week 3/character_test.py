from character import Character, Enemy
dave = Enemy("Dave", "A smelly zombie")

dave.describe()
#Conversation
dave.set_conversation("*zombie grunts*")
dave.talk()

dave.set_weakness("sword")
print("What will you fight with?")
fight_with = input()
dave.fight(fight_with)