from turtle import Turtle
import random
import time

angels = list(range(0, 30)) + list(range(151, 210)) + list(range(331, 361))
angel = random.choice(angels)

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.y_move = 15
        self.x_move = 15
        self.speed(0)
        self.move_speed = 0.1
         
    def move(self):
        y_cord = self.ycor() + self.y_move
        x_cord = self.xcor() + self.x_move
        self.goto(x_cord, y_cord)
        
    def bounce(self):
        self.y_move *= -1
        
    def disc_bounce(self):
        self.x_move *= -1 
        self.move_speed *= 0.9   
        
    def restart(self):
        self.goto(0, 0) 
        self.disc_bounce()  
        self.move_speed = 0.1 
        
        