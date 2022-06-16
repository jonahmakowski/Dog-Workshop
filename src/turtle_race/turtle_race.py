import turtle
from random import randint as r
import time

Helper = turtle.Turtle()
Red = turtle.Turtle()
Blue = turtle.Turtle()
Green = turtle.Turtle()

Red.color('red')
Blue.color('blue')
Green.color('green')

turtle_list = [Red, Blue, Green]

Helper.speed(0)
Helper.penup()
Helper.goto(-280, 280)
Helper.pendown()
for i in range(4):
    Helper.forward(200)
    Helper.right(90)
    Helper.forward(20)
    Helper.right(90)
    Helper.penup()
    Helper.forward(200)
    Helper.right(180)
    Helper.pendown()

y = 270

for item in turtle_list:
    item.shape('turtle')
    item.penup()
    item.goto(-280, y)
    y -= 20

for i in range(45):
    for item in turtle_list:
        item.forward(r(0, 10))

scores = [Red.xcor(),
          Blue.xcor(),
          Green.xcor()]

red = Red.xcor()
blue = Blue.xcor()
green = Green.xcor()

scores.sort(reverse=True)

place = 1

for item in scores:
    if item == red:
        print('{}. Red: {}'.format(place, item))
    elif item == blue:
        print('{}. Blue: {}'.format(place, item))
    elif item == green:
        print('{}. Green: {}'.format(place, item))
    place += 1

time.sleep(10)
