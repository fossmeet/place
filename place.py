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

##madhav
t = Turtle()
t.color("yellow")
t.penup()
t.setpos(100,100)
t.begin_fill()

t.circle(40, 300)
t.left(90)
t.forward(40)
t.right(120)
t.forward(40)
t.end_fill()

t.penup()


t.hideturtle()
##endmadhav

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



# spidy

color('red')
fillcolor('blue')
begin_fill()
fd(200)
left(90)
fd(5)
left(90)
fd(200)
left(5)
end_fill()
write("FOSSMEET", font=("Arial", 20, "normal"))
# my code

forward(20)
right(200)
forward(260)


# ------- -------- #
#  Nee shooperada! #
#------------------#
pen = Turtle()
pen.color("black")
pen.pensize(3)
pen.speed(0)
pen.hideturtle()
pen.penup()
pen.goto(-500,100)
pen.pendown()
pen.write("                       _                                      _", align="left", font=("monospace", 16, "bold"))
pen.penup()
pen.goto(-500,80)
pen.pendown()
pen.write(" _ __   ___  ___   ___| |__   ___   ___  _ __   ___ _ __ __ _  __| | __ _ ", align="left", font=("monospace", 16, "bold"))
pen.penup()
pen.goto(-500,60)
pen.pendown()
pen.write("| '_ \\ / _ \\ / _ \\ / __| '_ \\ / _ \\ / _ \\| '_ \\ / _ \\ '__/ _` |/ _` |/ _` |", align="left", font=("monospace", 16, "bold"))
pen.penup()
pen.goto(-500,40)
pen.pendown()
pen.write("| | | |  __/  __/ \\__ \\ | | | (_) | (_) | |_) |  __/ | | (_| | (_| | (_| |", align="left", font=("monospace", 16, "bold"))
pen.penup()
pen.goto(-500,20)
pen.pendown()
pen.write("|_| |_|\\___|\\___| |___/_| |_|\\___/ \\___/| .__/ \\___|_|  \\__,_|\\__,_|\\__,_|", align="left", font=("monospace", 16, "bold"))
pen.penup()
pen.goto(-500,0)
pen.pendown()
pen.write("                                        |_|                               ", align="left", font=("monospace", 16, "bold"))

# ------- -------- #
#      end         #
# nee shooperada   #
#------------------#


# Debian - Spiral Helix
colors = ['red', 'purple', 'blue', 'green', 'orange', 'yellow']
def create_spiral_helix():
    setx(0)
    sety(0)
    speed(0)
    for i in range(10):
        setx(20*i)
        sety(20*i)
        fillcolor(colors[i%6])
        begin_fill()
        circle(50*i)
        circle(-50*i)
        left(i)
        end_fill()
    speed(0)

create_spiral_helix()
if __name__ == "__main__":
    create_spiral_helix()
else:
    create_spiral_helix()

#LEAF VILLAGE MWUHAHAHA

a = Turtle()
a.penup()
a.goto(0,300)
a.pendown()
a.width(5)


for i in range(38):
    a.forward(i)
    a.right(20)

a.left(90)
a.forward(100)
a.penup()
a.goto(-100,300)
a.pendown()
a.right(150)
a.forward(100)
a.left(113)
a.forward(100)

a.penup()
a.goto(0,0)
a.pendown()

#Ashwin
red =Turtle()

red.right(1)
red.forward(2)
red.right(2)
red.forward(2)
red.right(2)
red.forward(2)
red.right(2)

setpos(100,100)
fillcolor('red')
begin_fill()
circle(34)
end_fill()

#Alen
def draw_star(size, x, y):

    penup()
    goto(x, y)
    pendown()
    for i in range(5):
        forward(size)
        right(144)

draw_star(10, 300, 100)

# Rithas K
# Sorry for the long lines :)
home()
penup()
goto(320, -170)
pendown()
left(60)
forward(100)
right(90)
forward(75)
right(90)
forward(20)
right(90)
forward(50)
left(90)
forward(20)
left(90)
forward(50)
right(90)
forward(20)
right(90)
forward(50)
left(90)
forward(40)
right(90)
forward(25)

left(135)
forward(20)
left(45)
forward(25)
left(135)
forward(20)

left(180)
forward(20)
left(135)
forward(40)
left(45)
forward(20)

left(180)
forward(20)
left(45)
forward(50)
left(135)
forward(20)

left(180)
forward(20)
left(135)
forward(20)
left(45)
forward(20)

penup()
goto(382, -114)
pendown()

left(180)
forward(20)
right(45)
forward(5)

left(180)
forward(5)
right(90)
forward(50)
left(135)
forward(20)

left(180)
forward(20)
left(135)
forward(20)
left(45)
forward(20)