from turtle import Turtle



UP=90
DOWN=270

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(5, 1)
        self.penup()
        self.create_paddle(position)

    def create_paddle(self,pos):
        self.goto(pos)

    def move_up_paddle(self):
        new_y= self.ycor() + 20
        self.goto(self.xcor(), new_y)

    def move_down_paddle(self):
        new_y = self.ycor() - 20
        self.goto(self.xcor(), new_y)
































