from turtle import Turtle

STARTING_POSITION = (0, -250)

class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.shape("circle")
        self.pu()
        self.x_move = 10
        self.y_move = 12
        self.ball_speed = 0.04
        self.goto(STARTING_POSITION)

    def move(self):
        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.x_move *= -1

    def hit(self):
        self.y_move *= -1

    def reset_position(self):
        self.goto(STARTING_POSITION)
        self.x_move = 10
        self.y_move = 12

    def miss(self):
        self.reset_position()
