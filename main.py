from turtle import Turtle, Screen
from ball import Ball
from paddle import Paddle
from board import Board
from scoreboard import Scoreboard
import time

is_game_on = True


def game_end():
    global is_game_on
    is_game_on = False
    screen.clear()


screen = Screen()
screen.setup(width=500, height=600)
screen.bgcolor("black")
screen.title("Breakout")
screen.tracer(0)
screen.listen()


paddle = Paddle()
ball = Ball()
board = Board()
scoreboard = Scoreboard()
screen.onkey(key="Left", fun=paddle.go_left)
screen.onkey(key="Right", fun=paddle.go_right)
screen.onkey(key="Escape", fun=game_end)


while is_game_on:
    time.sleep(ball.ball_speed)
    screen.update()
    ball.move()
    if ball.xcor() > 240 or ball.xcor() < -240:
        ball.bounce()
    if ball.ycor() > 280:
        ball.hit()
    if board.check_collision(ball):
        ball.hit()
        scoreboard.score()
        if len(board.all_tiles) == 0:
            is_game_on = False
            screen.update()
            scoreboard.game_over("You win!")
    if ball.ycor() < -260:
        if ball.distance(paddle) < 55:
            ball.hit()
    if ball.ycor() < -280:
        ball.miss()
        scoreboard.lose_life()
        if scoreboard.lives == 0:
            is_game_on = False
            scoreboard.game_over("You Lose.")

screen.exitonclick()
