import turtle

paper = turtle.Screen()
michelangelo = turtle.Turtle()
michelangelo.speed(20)
michelangelo.penup()
michelangelo.goto(50,50)
michelangelo.pendown()

donatello = turtle.Turtle()
donatello.speed(20)

donatello.penup()
donatello.goto(-100,-100)
donatello.pendown()

# This is the first mandala, and it's in black and white because I prefer how it looks
# but there is also a colored one below just to demonstrate my skills

# Black and white mandala
for element in range(18):
    michelangelo.circle(50)
    michelangelo.left(25)

for element in range(23):
    michelangelo.circle(40)
    michelangelo.left(20)

for element in range(27):
    michelangelo.circle(30)
    michelangelo.left(15)

for element in range(36):
    michelangelo.circle(10)
    michelangelo.left(10)

# Colored Mandala
for element in range(18):
    donatello.color("blue")
    donatello.circle(50)
    donatello.left(25)

for element in range(23):
    donatello.color("red")
    donatello.circle(40)
    donatello.left(20)

for element in range(27):
    donatello.color("orange")
    donatello.circle(30)
    donatello.left(15)

for element in range(36):
    donatello.color("yellow")
    donatello.circle(10)
    donatello.left(10)

paper.exitonclick()
