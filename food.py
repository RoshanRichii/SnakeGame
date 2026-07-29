#snake_food
import random
from turtle import Turtle


class Food(Turtle):
    def __init__(self, score_tab=None):
        super().__init__()
        self.score_tab = score_tab
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

    def reset(self):
        self.refresh()

    def snake_food_collision(self, snake):
        if self.distance(snake.segments[0]) < 15:
            self.reset()
            snake.extend()
            if self.score_tab is not None:
                self.score_tab.increase_score()
    