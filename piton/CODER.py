import turtle
import random
t = turtle.Turtle()

r = turtle.Turtle()

t.speed(0)

r.hideturtle()
t.hideturtle()
t.penup()
t.backward(50)
t.right(90)
t.forward(100)
t.left(90)
t.pendown()

for i in range (0,2):
    t.forward (100)
    t.left (90)
    t.forward(200)
    t.left(90)

t.penup()
t.forward(15)
t.left(90)
t.forward(20)
t.right(90)
t.pendown()
color = ["#E60000", "#E62600", "#E64C00", "#E67300", "#E69900", "#E6BF00", "#E6E600", "#BFE600", "#99E600", "#73E600", "#4CE600", "#26E600", "#00E600", "#00E626", "#00E64D", "#00E673", "#00E699", "#00E6BF", "#00E6E6", "#00BFE6", "#0099E6", "#0073E6", "#004DE6", "#0026E6", "#0000E6", "#2600E6", "#4C00E6", "#7300E6", "#9900E6", "#BF00E6", "#E600E6", "#E600BF", "#E60099", "#E60073", "#E6004C", "#E60026"]

j = 0

while True :

    #if j >= color.__len__() - 1:
    #    j = 0
    #else:
    #    j += 1

    #couleur = color[j]

    color = random.randint(0,255), random.randint(0,255), random.randint(0,255)

    t.pencolor(color)
    t.fillcolor(color)
    t.begin_fill() 
    t.forward(70)
    t.left(115)
    t.forward(170)  
    t.right(115)
    t.forward(70)
    t.right(114)
    t.forward(170)
    t.left(114)
    t.goto (-35,-80)
    t.end_fill()

t.hideturtle()
while True :
    r.left(1)