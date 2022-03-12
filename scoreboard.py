from turtle import Turtle

class Board(Turtle):
    def __init__(self) :
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()   
        self.setposition(0,280)
        self.score=0
        self.highscore = 0 
        self.highscore_check()
        self.write(f"POINTS = {self.score} - HIGHSCORE = {self.highscore }", False, align="center", font='Arial')

    def score_update(self):
        self.highscore_check()
        self.score +=1 
        self.clear()
        
        self.write(f"POINTS = {self.score} - HIGHSCORE = {self.highscore + 1}", False, align="center", font='Arial')
        self.highscore_check()
    def game_over(self): 
        self.goto(0,0)
        self.write(f"GAME OVER", False, align="center", font='Arial')
    def highscore_check(self) : 
        data = open("data.txt" , mode="r")
        self.highscore = data.read()
        
        data.close()
        self.highscore=int(self.highscore)
        if self.score > self.highscore : 
            with open("data.txt" , mode="w") as data : 
               data.write(f"{self.score}")
        
