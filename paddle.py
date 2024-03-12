from turtle import Turtle

class Paddle(Turtle):
    def __init__(self,position):
        super().__init__()

        self.shape("square")
        self.color("white")
        self.shapesize(5,1)
        self.penup()
        self.goto(position)
        self.Up()
        self.Down()



    def Up(self):
        y_cor=self.ycor()+20
        self.goto(self.xcor(),y_cor)
    def Down(self):
        y_cor=self.ycor()-20
        self.goto(self.xcor(),y_cor)

