import turtle
from turtle import Turtle, dot, Screen
import random
#set screen and turtle characteristics
screen= Screen()
timmy= Turtle()
timmy.shape("turtle")
timmy.color("red")
screen.screensize(400,400)
screen.colormode(255)
choices = random


def random_color():
    return choices.randint(0,255)
#set pen color and turtle speed
timmy.pensize(1)
timmy.speed(0)

#function to choose random point on screed and make spiralgraph drawing with random colors for each circle then pick another spot
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

