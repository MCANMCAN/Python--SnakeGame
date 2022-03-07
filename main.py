from turtle import Screen,Turtle
from scoreboard import Board
from snake import Snake
from food import Food

import time
screen = Screen()
screen.setup(width=600,height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)
mysnake=Snake()
text = Board()
foody = Food()
screen.listen() 
screen.onkey(mysnake.up,"Up")
screen.onkey(mysnake.down,"Down")
screen.onkey(mysnake.left,"Left")
screen.onkey(mysnake.right,"Right")
game =True
while game == True:
    screen.update()
    time.sleep(0.1)
    mysnake.move()
    if mysnake.heading.distance(foody) < 15 :
        foody.randompos()
        text.score_update()
        mysnake.extend()

    if mysnake.heading.xcor() >= 290 or mysnake.heading.xcor() <= -290 or mysnake.heading.ycor() <= -290 or mysnake.heading.ycor() >= 290: 
        game=False
        text.game_over()
    
    for segment in mysnake.segments[1:] : 
        if mysnake.heading.distance(segment) < 10 : 
            game=False
            text.game_over()



    
    
    

        




















screen.exitonclick()