import turtle as t
pen = t.Turtle()
t.Screen().setup(width=1.0, height=1.0)
t.speed(0)
t.fillcolor('#1793d1')
t.begin_fill()
t.penup()
t.sety(-170)
t.setpos((-640, 512))
t.setx(640)
t.setpos((0, -170))
t.end_fill()

t.fillcolor('#d70a53')
t.begin_fill()
t.sety(-512)
t.setx(640)
t.sety(512)
t.end_fill()

t.setx(-640)

t.fillcolor('#072c61')
t.begin_fill()
t.sety(-512)
t.setx(0)
t.sety(-170)
t.end_fill()
pen.color('#ffe4e1')
pen.begin_fill()
pen.left(42)
pen.forward(120)
pen.circle(80, 190)
pen.right(100)
pen.circle(80, 180)
pen.forward(160)
pen.left(90)
pen.forward(50)
pen.setpos(-60, 100)
pen.end_fill()
def txt():
    pen.up()
    pen.setpos(-60, 100)
    pen.color('red')
    pen.write("FOSSMEET'23", font=("Comic Sans MS", 16))
txt()
pen.end_fill()
t.exitonclick()
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
pen.speed(10)
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
        fillcolor(colors[i%6])
        begin_fill()
        circle(5*i)
        circle(-5*i)
        left(i)
        end_fill()
    speed(5)

create_spiral_helix()
if __name__ == "__main__":
    create_spiral_helix()
else:
    create_spiral_helix()


#Ashwin
red =Turtle()

red.right(1)
red.forward(2)
red.right(2)
red.forward(2)
red.right(2)
red.forward(2)
red.right(2)


#Alen
def draw_star(size, x, y):

    penup()
    goto(x, y)
    pendown()
    for i in range(5):
        forward(size)
        right(144)

speed("fastest")

draw_star(10, 300, 100)
