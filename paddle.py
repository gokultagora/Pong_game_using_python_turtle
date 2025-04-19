import turtle

class Paddle(turtle.Turtle):
    def __init__(self, x, y):
        super().__init__()  # Initialize the parent Turtle class
        self.color("white")  # Set the color of the paddle
        self.shape("square")  # Shape of the paddle
        self.speed(0)  # Set the speed of the paddle
        self.shapesize(stretch_wid=5, stretch_len=0.5)  # Resize the paddle
        self.penup()  # Don't leave a trail
        self.goto(x, y)  # Set the initial position of the paddle

    def go_up(self):
        new_y = self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def go_down(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)

