from turtle import forward,right,penup,pendown,left,backward


penup()
right(180)
forward (300)
right(180)
pendown()

def polygone_regulier():
    for i in range(4):
        left(90)
        if i%2 == 0:
            forward(50)
        else:
            forward(100)

def hexagone():
    for i in range(6):
        forward(75)
        left(60)

def le_truc():
    for i in range(6):
        right(60)
        forward(100)
        backward(100)

polygone_regulier()

penup()
forward (200)
pendown()

hexagone()

penup()
forward (350)
left(90)
forward (50)
right(90)
pendown()

le_truc()

while True :
    right(1)