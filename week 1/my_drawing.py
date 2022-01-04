from shapes import Paper, Triangle, Rectangle, Oval

paper = Paper()

#Creating rectangle 1
sky = Rectangle(600,600,0,0,"lightskyblue")
sky.draw()

#Creating rectangle 2
grass = Rectangle(600,200,0,400,"limegreen")
grass.draw()

#Creating an oval
sun = Oval(100,100,50,50,"yellow")
sun.draw()

#Creating rectangle 3
house_foundation = Rectangle(250,200,250,250,"bisque")
house_foundation.draw()

#Creating triangle 1
roof = Triangle(375,100,500,250,250,250,"brown")
roof.draw()

#Creating rectangle 4
door = Rectangle(50,100,350,350,"sienna")
door.draw()

paper.display()
