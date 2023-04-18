from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 15, "bold")
GAME_OVER_FONT = ("Courier", 30, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.SCORE = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.goto(x=0, y=270)
        self.score()

    def score(self):
        self.write(arg=f"Score: {self.SCORE}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write(arg="GAME OVER!!!", align=ALIGNMENT, font=GAME_OVER_FONT)

    def add_score(self):
        self.clear()
        self.SCORE += 1
        self.score()
