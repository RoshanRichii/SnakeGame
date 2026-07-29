from turtle import Turtle


class ScoreTab(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.update_display()

    def update_display(self):
        self.clear()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center", font=("Arial", 16, "bold"))
        self.goto(220, 280)
        self.write(f"High Score: {self.high_score}", align="right", font=("Arial", 10, "normal"))

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            self.high_score = self.score
        self.update_display()

    def reset_score(self):
        self.score = 0
        self.update_display()