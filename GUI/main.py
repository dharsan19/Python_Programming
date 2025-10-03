from turtle import Turtle, Screen

timmy = Turtle()
timmy.shape("turtle")
timmy.color("cyan")

def timmy_move():
    timmy.forward(100)
    timmy.left(90)

for i in range(4):
    timmy_move()

screen = Screen()
screen.exitonclick()