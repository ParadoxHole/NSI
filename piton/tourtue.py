import turtle as t

bonjour = t.Turtle()
bonjour.penup()
bonjour.right(180)
bonjour.forward (300)
bonjour.right(180)
bonjour.pendown()

def polygone_régulier():
    for i in range(4):
        bonjour.left(90)
        if i%2 == 0:
            bonjour.forward(50)
        else:
            bonjour.forward(100)


def hexagone():
    for i in range(6):
        bonjour.forward(75)
        bonjour.left(60)

def le_truc():
    for i in range(6):
        bonjour.right(60)
        bonjour.forward(100)
        bonjour.backward(100)

polygone_régulier()

bonjour.penup()
bonjour.forward (200)
bonjour.pendown()

hexagone()

bonjour.penup()
bonjour.forward (350)
bonjour.left(90)
bonjour.forward (50)
bonjour.right(90)
bonjour.pendown()

le_truc()

while True :
    bonjour.right(1)