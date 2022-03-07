from turtle import Turtle

class Board(Turtle):
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()   
        self.setposition(0,280)
        self.score=0
        self.write(f"POINTS = {self.score} ", False, align="center", font='Arial')
    def score_update(self):
        self.score +=1 
        self.clear()
        self.write(f"POINTS = {self.score} ", False, align="center", font='Arial')
    def game_over(self): 
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font='Arial')

