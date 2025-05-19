from turtle import Turtle

ALLIGNMENT = "center"
FONT = ('Courier', 48, 'normal')

class ScoreBoard(Turtle):
    def __init__(self, x_cord, y_cord):
        super().__init__()
        self.goto(x=x_cord, y=y_cord)
        self.score = 0
        self.pencolor("white")
        self.penup()
        self.ht()
        self.write(self.score, align=ALLIGNMENT, font=FONT)

    def update(self):
        self.clear()
        self.score +=1
        self.write(f"{self.score}", align=ALLIGNMENT, font=FONT)
        
    def over(self):    
        self.goto(0, 0)
        self.write(f"Game Over", align=ALLIGNMENT, font=FONT)
        