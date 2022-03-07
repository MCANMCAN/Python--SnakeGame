from turtle import Turtle
import random          


class Food(Turtle) : 

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.penup()
        self.randompos()
    def randompos(self): 
        fposx = random.randint(-270,270)
        fposy = random.randint(-270,270)
        self.goto(fposx,fposy)