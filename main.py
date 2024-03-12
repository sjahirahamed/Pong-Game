from turtle import Screen
from paddle import Paddle
from ball_move import Ball
from scoreboard import Score
import time
screen=Screen()
"""this block which describe about the screen size and the color"""

# screen.screensize(800,600)
screen.setup(800,600)

screen.bgcolor("black")
screen.title("Pong_Game")
screen.listen()
screen.tracer(0) #it turn of all animation on screen

rp=Paddle((350,0))
lp=Paddle((-350,0))
ball=Ball()
score=Score()

"""this key for moving up and down it required screen.listen for screen.onkey"""
#For right paddle
screen.onkey(rp.Up, "Up")
screen.onkey(rp.Down, "Down")
#For left paddle
screen.onkey(lp.Up,"w")
screen.onkey(lp.Down,"s")


game_is_on=True
while game_is_on:
    time.sleep(ball.ball_moveing_speed)
    screen.update()#which is use to update the screen
    ball.move_ball()
    #Detect the collision top and bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y() # bounce the ball

    #Detect the collision from right and left paddle
    if ball.distance(rp) < 50 and ball.xcor() > 330 or ball.distance(lp) < 50 and ball.xcor() < -330:
        ball.bounce_x()
    #Detect when paddle misses ball of right paddle
    if ball.xcor() > 380:
        ball.reset_position()
        score.l_point()

    #Detect when paddle misses ball of left paddle
    if ball.xcor() < -380:
        ball.reset_position()
        score.r_point()




screen.exitonclick()