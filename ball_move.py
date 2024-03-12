from turtle import Turtle
import time



class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shapesize(0.5, 0.5)
        self.color("white")
        self.shape("circle")
        self.penup()
        self.x_vau = 10
        self.y_vau = 10
        self.ball_moveing_speed=0.1





    def move_ball(self):
        x_cor=self.xcor()+self.x_vau
        y_cor=self.ycor()+self.y_vau
        self.goto(x_cor,y_cor)
    def bounce_y(self):
        self.y_vau *= -1
    def bounce_x(self):
        self.x_vau *= -1
        self.ball_moveing_speed *= 0.95
    def reset_position(self):
        self.goto(0,0)
        self.ball_moveing_speed=0.1
        self.bounce_x()


