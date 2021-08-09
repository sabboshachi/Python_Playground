import turtle
turtle.shape("turtle")
turtle.speed(2)

for length in range(50,500,10):
    for i in range(4):
        turtle.forward(length)
        turtle.left(90)
turtle.exitonclick()






