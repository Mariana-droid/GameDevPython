from turtle import Turtle
from turtle import Screen
from random import randint

background = Screen()
background.colormode(255)
background.bgcolor("black")

def random_color():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)
    return (r,g,b)

#Creating objects of turtle
grisha = Turtle()
grisha.color("yellow")
grisha.shape("turtle")

suli = Turtle()
suli.color("purple")
suli.shape("turtle")

druskelle = Turtle()
druskelle.color("blue")
druskelle.shape("turtle")

crow = Turtle()
crow.color("gray")
crow.shape("turtle")

#Turtle preparing for the race 

grisha.penup()
grisha.goto(-160,100)
grisha.pendown()

suli.penup()
suli.goto(-160,70)
suli.pendown()

druskelle.penup()
druskelle.goto(-160,40)
druskelle.pendown()

crow.penup()
crow.goto(-160,10)
crow.pendown()

#Race
for movement in range(100):
    grisha.forward(randint(1,5))
    grisha.color(random_color()) #giving it some spice

    suli.forward(randint(1,5))
    druskelle.forward(randint(1,5))
    crow.forward(randint(1,5))

input("Press enter to close")