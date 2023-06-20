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
        self.goto(60, 270)
        self.pd()
        self.write("Lives: ", font=SCOREBOARD_FONT)
        self.pu()
        x = self.xcor() + 92
        for _ in range(self.lives):
            self.goto(x, 267)
            self.write("❤️", font=SCOREBOARD_FONT)
            x += 30
        self.hideturtle()

    def score(self):
        self.current_score += 2
        self.update_scoreboard()

    def lose_life(self):
        self.lives -= 1
        self.update_scoreboard()

    def game_over(self, condition):
        self.goto(0, 0)
        if self.lives == 0:
            final_score = self.current_score
        else:
            final_score = self.current_score * self.lives
        self.write(f"Game Over. {condition}\nFinal Score: {final_score}", align="center", font=SCOREBOARD_FONT)

