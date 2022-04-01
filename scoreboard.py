from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.level = 1
        self.penup()
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-290, 260)
        self.write(f"LEVEL:{self.level}", align='left', font=FONT)

    def main_score(self):
        self.level += 1
        self.update_score()
