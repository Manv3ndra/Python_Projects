import turtle
import random

class Food(turtle.Turtle):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(0.5, 0.5)
        self.color('red')
        self.speed('fastest')
        self.refresh()
    
    def refresh(self):
        x = random.randint(-280, 280)
        y = random.randint(-280, 260)
        self.goto(x,y)