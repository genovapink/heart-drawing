import turtle
import math

screen = turtle.Screen()
screen.bgcolor("black")

pen = turtle.Turtle()
pen.speed(0)
pen.color("pink")

def draw_heart():
    pen.penup()
    pen.goto(0, -100)
    pen.pendown()
    for i in range(100):
        angle = math.radians(i * 4)
        x = 16 * math.sin(angle) ** 3
        y = 13 * math.cos(angle) - 5 * math.cos(2 * angle) - 2 * math.cos(3 * angle) - math.cos(4 * angle)
        pen.goto(x * 10, y * 10)
    pen.penup()

for i in range(10):
    pen.width(i)
    draw_heart()

pen.hideturtle()

turtle.done()
