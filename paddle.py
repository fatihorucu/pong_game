from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.color("white")
        self.shape("square")
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.setposition(coordinates)

    def up(self):
        new_y = self.ycor() + 20
        self.setposition(self.xcor(), new_y)

    def down(self):
        new_y = self.ycor() - 20
        self.setposition(self.xcor(), new_y)
