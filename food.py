from random import randint
from turtle import Turtle

class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(0.5)
        self.color("white")
        self.speed("fastest")
        self.refresh()


    def refresh(self):
        x = randint(-330, 330)
        y = randint(-330, 330)
        self.goto(x, y)







