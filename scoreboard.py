from turtle import Turtle

class ScoreBoard(Turtle):

    def __init__(self, x, player_label):
        super().__init__()
        self.color("white")
        self.penup()
        self.goto(x, 270)
        self.hideturtle()
        self.score = 0
        self.player_label = player_label  # Store label for display
        self.update_score()

    def update_score(self):
        self.clear()
        self.write(f"{self.player_label} : {self.score}", align="center", font=("courier", 15, "bold"))

    def refresh(self):
        self.score += 1
        self.update_score()

    def game_over(self, player):
        self.goto(0, -35)
        self.write(f"****GAME OVER****\n\n{player} has won!", align="center", font=("courier", 15, "bold"))
