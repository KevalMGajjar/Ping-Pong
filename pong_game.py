from turtle import Screen
from pong import Pong
import time
from disc import Disc
from ball import Ball
from score_board import ScoreBoard

my_screen = Screen()
my_screen.bgcolor("black")
my_screen.setup(width=900, height=500)
my_screen.title("Pong Game")
game_state = True

my_screen.tracer(0)
pong = Pong()
disc_1 = Disc(420, 0)
disc_2 = Disc(-420, 0)
ball = Ball()
player1_score = ScoreBoard(50, 180)
player2_score = ScoreBoard(-50, 180)
my_screen.update()

my_screen.listen()
my_screen.onkeypress(fun=disc_1.forward, key="Up")
my_screen.onkeypress(fun=disc_1.backward, key="Down")
my_screen.onkeypress(fun=disc_2.forward, key="w")
my_screen.onkeypress(fun=disc_2.backward, key="s")



while game_state == True:
    time.sleep(ball.move_speed)
    my_screen.update()
    ball.move()
    if ball.ycor() > 235 or ball.ycor() < -235:
        ball.bounce()
        
    if ball.xcor() > 390 and disc_1.distance(ball) < 50 or ball.xcor() < -390 and disc_2.distance(ball) < 50:
        ball.disc_bounce() 
        
    if ball.xcor() > 470:
        player2_score.update()  
        ball.restart()
          
    if ball.xcor() < -470:
        player1_score.update()
        ball.restart()
    
    if player1_score.score == 10 or player2_score.score == 10:
        player1_score.over()
        game_state = False    
    
my_screen.exitonclick()