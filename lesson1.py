from turtle import *

#we want to print a house

#step 1: draw a square

penup()
goto(-100, -100)
pendown()

speed(30)
width(7)
color("blue")

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)

forward(200)
left(90)
#end of square

#drawing a door
forward(70)
color("orange")
begin_fill()
left(90)
forward(110)           #height of the door
right(90)
forward(60)              
right(90)
forward(110)
end_fill()

penup()
goto(100, 100)
pendown()

color("green")
begin_fill()
right(150)
forward(200)
left(120)
forward(200)
end_fill()

#drawing a windows

#first window
penup()
goto(-80, 25)
pendown()

color("orange")

right(150)
forward(50)

right(90)
forward(35)

right(90)
forward(50)

right(90)
forward(35)

#second window
penup()
goto(45, 25)
pendown()

right(90)
forward(50)

right(90)
forward(35)

right(90)
forward(50)

right(90)
forward(35)

penup()
goto(80, 50)
pendown()

forward(35)

penup()
goto(62.5, 75)
pendown()

left(90)
forward(50)

penup()
goto(-80, 50)
pendown()

left(90)
forward(35)

penup()
goto(-62.5, 75)
pendown()

right(90)
forward(50)
exitonclick()