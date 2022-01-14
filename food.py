from turtle import Turtle
import random


class Food(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.color("blue")
        self.speed("fastest")
        self.rfh()

    def rfh(self):
        rax = random.randint(-280, 280)
        ray = random.randint(-280, 280)
        self.goto(rax, ray)
