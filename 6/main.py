import turtle

# Увеличение видимой области
turtle.setworldcoordinates(-15, -15, 15, 15)
turtle.speed(0)

# Сетка координат
for i in range(15):
    for j in range(15):
        turtle.penup()
        turtle.goto(i, -j)
        turtle.pendown()
        turtle.dot(2, 'black')
turtle.penup()
turtle.goto(0, 0)
turtle.pendown()

# Сама задача
for i in range(4):
    turtle.forward(14)
    turtle.right(120)

turtle.exitonclick()