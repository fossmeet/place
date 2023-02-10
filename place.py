from turtle import *
import random

Screen().setup(width=1.0, height=1.0)
speed(0)

fillcolor('#1793d1')
begin_fill()
penup()
sety(-170)
setpos((-640, 512))
setx(640)
setpos((0, -170))
end_fill()

fillcolor('#d70a53')
begin_fill()
sety(-512)
setx(640)
sety(512)
end_fill()

setx(-640)

fillcolor('#072c61')
begin_fill()
sety(-512)
setx(0)
sety(-170)
end_fill()

fillcolor('#00ff00')
begin_fill()
penup()
sety(-17)
setpos((-64, 5))
setx(16)
setpos((0, -7))
end_fill()

fillcolor('#08fee5')
begin_fill()
circle(23)
end_fill()

# my code

forward(20)
right(200)
forward(260)

#Ashwin
red =Turtle()
fillcolor('#08fee5')
begin_fill()
red.right(10)
red.forward(20)
red.left(20)
red.forward(20)
red.right(20)
end_fill()

def curve(): # Method to draw curve
    for i in range(20): # To draw the curve step by step
        red.right(1)
        red.forward(1)

def heart():  # Method to draw full Heart
    red.fillcolor('red')
    red.begin_fill()
    red.left(14)
    red.forward(11)
    curve() # Left Curve
    red.left(12)
    curve() # Right Curve
    red.forward(11)
    red.end_fill()

heart()
