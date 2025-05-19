from turtle import Turtle

class Disc(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.shape("square")
        self.setheading(90)
        self.color("white")
        self.shapesize(stretch_len=5, stretch_wid=1)
        self.penup()
        self.goto(x_cord, y_cord)
        
    def forward(self):
        y_cord = self.ycor()
        x_cord = self.xcor()
        if y_cord < 190:
            y_cord += 20
            self.goto(x=x_cord, y=y_cord)
        
    def backward(self):
        y_cord = self.ycor()
        x_cord = self.xcor()
        if y_cord > -190:
            y_cord -= 20
            self.goto(x=x_cord, y=y_cord)
            