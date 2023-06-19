from turtle import Turtle

LEFT = 180
RIGHT = 0
MOVE_DISTANCE = 40


class Paddle(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("square")
        self.setheading(LEFT)
        self.color("white")
        self.shapesize(stretch_wid=1, stretch_len=5)
        self.penup()
        self.setheading(RIGHT)
        self.goto(0, -270)

    def go_right(self):
        self.forward(MOVE_DISTANCE)

    def go_left(self):
        self.backward(MOVE_DISTANCE)