import turtle as t

patate = t.Turtle()
patate.penup()
patate.goto(200,0)
patate.setheading(20)
patate.pendown()

patate.begin_fill()
patate.lt(30)
patate.fd(100)
patate.rt(160)
patate.fd(115)
patate.rt(120)
patate.fd(40)
patate.lt(100)
patate.fd(40)
patate.rt(120)
patate.fd(115)
patate.end_fill()

patate.setheading(180)
patate.penup()
patate.forward(200)
patate.pendown()
patate.setheading(0)

patate.begin_fill()

for i in range(3):
    patate.right(300)
    patate.forward(75)

while True :
    patate.right(1)