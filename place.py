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

red.right(1)
red.forward(2)
red.right(2)
red.forward(2)
red.right(2)
red.forward(2)
red.right(2)

# Debian - Spiral Helix
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
def create_spiral_helix():
    setx(0)
    sety(0)
    speed(2)
    for i in range(100):
        fillcolor(colors[i%6])
        begin_fill()
        circle(5*i)
        circle(-5*i)
        left(i)
        end_fill()
    speed(0)

create_spiral_helix()
if __name__ == "__main__":
    create_spiral_helix()
else:
    create_spiral_helix()