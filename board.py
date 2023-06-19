from turtle import Turtle


class Tile(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.shapesize(stretch_wid=0.5, stretch_len=2)  # adjust as needed
        self.penup()
        self.goto(position)

    def erase(self):
        self.hideturtle()


class Board:
    def __init__(self):
        self.all_tiles = []
        self.create_board()

    def create_board(self):
        x_start = -230  # starting x position for the tiles
        y_start = 250   # starting y position for the tiles
        colors = ["orange", "orange", "pink", "pink", "teal", "teal"]
        for i in range(6):  # number of rows
            x = x_start
            y = y_start
            for _ in range(10):  # number of tiles per row
                tile = Tile((x, y))
                tile.color(colors[i])  # cycle through the colors list
                self.all_tiles.append(tile)
                x += 50  # space between tiles
            y_start -= 20  # space between rows

    def check_collision(self, ball):
        for tile in self.all_tiles:
            if ball.distance(tile) < 35:  # adjust this value based on your game's scale
                tile.erase()
                self.all_tiles.remove(tile)
                return True
        return False
