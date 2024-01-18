import turtle
from turtle import Turtle, dot, Screen
import random
screen= Screen()
timmy= Turtle()
timmy.shape("turtle")
timmy.color("red")
choices = random
direction = [0, 90, 180, 270]


def random_color():
    return choices.randint(0,255)


screen.colormode(255)

color1 = random_color()
color2 = random_color()
color3 = random_color()
timmy.pencolor(color1, color2, color3)
screen.screensize(400,400)
timmy.pensize(1)
timmy.speed(0)

for _ in range(10):
    timmy.penup()
    timmy.setposition(choices.randint(-350, 350), choices.randint(-350, 350))
    timmy.pendown()
    for _ in range(19):
        color1 = random_color()
        color2 = random_color()
        color3 = random_color()
        timmy.pencolor(color1, color2, color3)
        timmy.circle(50)
        timmy.left(20)

screen.exitonclick()

