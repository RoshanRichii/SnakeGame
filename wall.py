#wall-collision
from turtle import Turtle


class Wall(Turtle):
    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color("white")
        self.penup()
        self.goto(0, 0)
        self.game_over = False
        self.restart_callback = None

    def set_restart_callback(self, callback):
        self.restart_callback = callback

    def draw_game_over_box(self):
        self.clear()
        self.game_over = True
        self.color("white")
        self.pensize(3)
        self.penup()
        self.goto(-160, 80)
        self.pendown()
        for _ in range(2):
            self.forward(320)
            self.right(90)
            self.forward(160)
            self.right(90)

        self.penup()
        self.goto(0, 20)
        self.write("Game Over", align="center", font=("Arial", 24, "bold"))
        self.goto(0, -20)
        self.write("Try Again ↻", align="center", font=("Arial", 16, "normal"))

    def clear_game_over_box(self):
        self.game_over = False
        self.clear()

    def try_again(self, x, y):
        if not self.game_over:
            return
        if -160 <= x <= 160 and -80 <= y <= 80:
            self.clear_game_over_box()
            if self.restart_callback:
                self.restart_callback()

    def wall_collision(self, snake):
        head = snake.segments[0]
        if head.xcor() > 290 or head.xcor() < -290 or head.ycor() > 290 or head.ycor() < -290:
            self.draw_game_over_box()
            return True
        return False
