import turtle
import math

mercibaptiste = turtle.Turtle()

sides = [100, 200]

mercibaptiste.hideturtle()
mercibaptiste.forward(-sides[0]/2)
mercibaptiste.right(90)
mercibaptiste.forward(sides[1]/2)
mercibaptiste.right(-90)
mercibaptiste.pendown()
mercibaptiste.showturtle()

for i in range(0, 4):
    mercibaptiste.forward(sides[i % 2])
    mercibaptiste.left(90)

mercibaptiste.hideturtle()
mercibaptiste.penup()
mercibaptiste.forward(sides[0]/2)
mercibaptiste.right(-90)
mercibaptiste.forward(sides[1]/2)
mercibaptiste.right(90)

hypo = 150
base = 50
angle = math.degrees(math.asin(base/hypo))

mercibaptiste.forward(-base/2)
mercibaptiste.right(90)
mercibaptiste.forward(hypo/2)
mercibaptiste.right(-90)
mercibaptiste.pendown()
mercibaptiste.showturtle()

while True :
    mercibaptiste.color("#F")
    mercibaptiste.begin_fill()
    mercibaptiste.forward(base)
    mercibaptiste.left(90+angle)
    mercibaptiste.forward(hypo)
    mercibaptiste.right(90+angle)
    mercibaptiste.forward(base)
    mercibaptiste.right(90+angle)
    mercibaptiste.forward(hypo)
    mercibaptiste.end_fill()


while True:
    mercibaptiste.left(1)
