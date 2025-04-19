import turtle
from paddle import Paddle
from ball import Ball
from scoreboard import ScoreBoard
from court import CourtDrawer
import time

screen = turtle.Screen()
screen.bgcolor("black")
screen.setup(1000,600)
screen.tracer(0)

court = CourtDrawer()
court.draw_court()

player_1 = Paddle(450,0)
player_2 = Paddle(-450,0)
ball = Ball()
p1_score = ScoreBoard(100,"PLAYER I")
p2_score = ScoreBoard(-100,"PLAYER II")

screen.listen()
screen.onkey(player_1.go_up,"Up")
screen.onkey(player_1.go_down,"Down")

screen.onkey(player_2.go_up,"w")
screen.onkey(player_2.go_down,"s")

is_game_on = True
while is_game_on:
    time.sleep(0.05)
    screen.update()
    ball.move()

    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    if ball.distance(player_1) < 50 and ball.xcor() > 420 or ball.distance(player_2) < 50 and ball.xcor() < -420:
        ball.bounce_x()

    if ball.xcor() > 500:
        ball.refresh()
        p2_score.refresh()

    if ball.xcor() < -500:
        ball.refresh()
        p1_score.refresh()

    if p1_score.score == 7:
        is_game_on = False
        p1_score.game_over("PLAYER I")
    if p2_score.score == 7:
        is_game_on = False
        p2_score.game_over("PLAYER II")


screen.exitonclick()
