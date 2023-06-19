from turtle import Turtle

SCOREBOARD_FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.current_score = 0
        self.lives = 3
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.pu()
        self.goto(-240, 270)
        self.pd()
        self.write(f"Score: {self.current_score}", font=SCOREBOARD_FONT)
        self.pu()
        self.goto(80, 270)
        self.pd()
        self.write("Lives: ", font=SCOREBOARD_FONT)
        self.pu()
        x = self.xcor() + 100
        for _ in range(self.lives):
            self.goto(x, 270)
            self.write("X", font=SCOREBOARD_FONT)
            x += 20
        self.hideturtle()

    def score(self):
        self.current_score += 2
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self, condition):
        self.goto(0, 0)
        self.write(f"Game Over. {condition}", align="center", font=SCOREBOARD_FONT)
