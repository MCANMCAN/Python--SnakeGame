from turtle import Turtle , Screen
from snake import Snake
import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
mysnake=Snake()
screen.listen() 
screen.onkey(mysnake.up,"Up")
screen.onkey(mysnake.down,"Down")
screen.onkey(mysnake.left,"Left")
screen.onkey(mysnake.right,"Right")
while True:
    screen.update()
    time.sleep(0.1)
    mysnake.move()
    
    

        




















screen.exitonclick()