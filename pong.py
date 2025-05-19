from turtle import Turtle

class Pong(Turtle):
    def __init__(self):
        super().__init__()
        self.intersection()
        
    def intersection(self):
        intersection = Turtle()
        intersection.pencolor("white")
        intersection.pensize(5)
        intersection.penup()
        intersection.goto(x=0, y=250)
        intersection.pendown()
        intersection.setheading(270)
        for _ in range(25):
            intersection.forward(10)
            intersection.penup()
            intersection.forward(10)
            intersection.pendown()
            
        

        
        
                    
            

                