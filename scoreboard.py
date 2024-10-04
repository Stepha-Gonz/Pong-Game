from turtle import Turtle
class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.scorer=0
        self.scorel=0
        self.setpos(0,270)
        
    def score(self):
        self.write(f"{self.scorel}:{self.scorer}",font=('Arial', 20, 'normal'))
        
    def rpaddle_increment(self):
        
        self.scorer+=1
        self.clear()
        self.write(f"{self.scorel}:{self.scorer}",font=('Arial', 20, 'normal'))
        
    def lpaddle_increment(self):
        
        self.scorel+=1
        self.clear()
        self.write(f"{self.scorel}:{self.scorer}",font=('Arial', 20, 'normal'))   
        
        
    def game_over(self):
        self.goto(-50,0)
        if self.scorer>self.scorel:
            self.write("Right paddle won",font=('Arial', 15, 'normal'))
        elif self.scorer<self.scorel:
            self.write("Left paddle won",font=('Arial', 15, 'normal'))