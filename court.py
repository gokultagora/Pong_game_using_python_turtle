# court.py

from turtle import Turtle

class CourtDrawer(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.speed(0)
        self.pensize(3)

    def draw_court(self):
        # Draw outer rectangle
        x = 500
        y = 300
        self.color("white")
        self.penup()
        self.goto(x, y)
        self.setheading(-90)
        self.pendown()
        self.forward(2 * y)
        self.right(90)
        self.forward(2 * x)
        self.right(90)
        self.forward(2 * y)
        self.right(90)
        self.forward(2 * x)

        # Center line
        self.penup()
        self.goto(0, y)
        self.setheading(-90)
        self.pendown()
        self.forward(2 * y)

        # Center circle (radius = 60)
        self.penup()
        self.goto(0, -150)
        self.setheading(0)
        self.pendown()
        self.circle(150)

        #small inner circle
        self.penup()
        for i in range(1,11):
            self.goto(0, -i)
            self.setheading(0)
            self.pendown()
            self.circle(i)

        #scoreboard
        self.penup()
        self.goto(100,270)
        self.pendown()
        self.forward(80)
        self.left(90)
        self.forward(25)
        self.left(90)
        self.forward(370)
        self.left(90)
        self.forward(25)
        self.left(90)
        self.forward(300)



