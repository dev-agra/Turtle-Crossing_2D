from turtle import Turtle


class Line1(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('black')
        self.penup()
        self.goto(x=-300, y=-220)
        self.shapesize(stretch_wid=0.1, stretch_len=60)


class Line2(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x=0, y=-220)
        self.shapesize(stretch_wid=0.1, stretch_len=2)


class Line3(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('black')
        self.penup()
        self.goto(x=-280, y=240)
        self.shapesize(stretch_wid=0.1, stretch_len=60)


class Line4(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('square')
        self.color('white')
        self.penup()
        self.goto(x=0, y=240)
        self.shapesize(stretch_wid=0.1, stretch_len=2)
