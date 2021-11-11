from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)

def turn_left():
    tim.left(10)

def turn_right():
    tim.right(10)

def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()

def backwards():
    tim.forward(-10)

screen.listen()
screen.onkey(key="space", fun=move_forwards)
screen.onkey(key="w", fun=turn_left)
screen.onkey(key="d", fun=turn_right)
screen.onkey(key="s", fun=backwards)
screen.onkey(key="c", fun=clear)











screen.exitonclick()
