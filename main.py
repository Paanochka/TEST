import random
from turtle import *
from random import randint
import colorgram
from colorgram import Color

turt = Turtle()
turt.speed('fastest')
turt.shape('turtle')
colormode(255)
color_rgb = [(42, 32, 22), (23, 26, 33), (124, 89, 58), (52, 92, 151), (232, 240, 235), (181, 162, 123), (35, 27, 31), (227, 226, 205), (221, 164, 18), (24, 32, 28), (237, 224, 78), (223, 229, 233), (143, 22, 9), (6, 191, 225), (45, 54, 115), (251, 206, 0), (111, 167, 192), (74, 107, 95), (140, 172, 155), (36, 112, 235)]


def rand_color():
    return random.choice(color_rgb)


turt.penup()
turt.setposition(-300, -300)
change_pos = 0
for step in range(10):
    for _ in range(10):
        turt.fd(50)
        turt.dot(20, rand_color())
        change_pos += 5
    turt.setposition(-300, -300 + change_pos)








screen = Screen()
screen.exitonclick()