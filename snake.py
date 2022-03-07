from turtle import Turtle
STARTING_POS=[(0,0),(-20,0),(-40,0)]
MOVE_POS = 20
UP=90
DOWN = 270
LEFT = 180
RIGHT = 0  
class Snake: 
    "models snake and movements. "
    def __init__(self):
        self.segments=[]
        self.create_snake()
        self.heading=self.segments[0]
    def create_snake(self):
        for position in STARTING_POS :
          self.add_segment(position) 
            
    def add_segment(self,position):
        new_segment=Turtle(shape="square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)
    def extend(self):
        self.add_segment(self.segments[-1].position())
    
    def move(self): 
        for segnum in range(len(self.segments)-1,0,-1): 
            newx = self.segments[segnum - 1].xcor() 
            newy = self.segments[segnum - 1].ycor() 
            self.segments[segnum].goto(newx,newy)
        self.heading.forward(MOVE_POS) 
    
    def up(self):
      if self.heading.heading() != DOWN:
        self.heading.setheading(UP)
        self.move()
    def down(self):
      if self.heading.heading() != UP :
        self.heading.setheading(DOWN)
        self.move()    
    def left(self):
      if self.heading.heading() != RIGHT :
        self.heading.setheading(LEFT)
        self.move()
    def right(self):
      if self.heading.heading() != LEFT:
        self.heading.setheading(RIGHT)
        self.move()        