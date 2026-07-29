from turtle import Screen
import time
from snake import Snake
from food import Food
from wall import Wall
from scoretab import ScoreTab

score_tab = ScoreTab()
food = Food(score_tab)
wall = Wall()

screen = Screen()
screen.setup(600, 600)
screen.bgcolor("black")
screen.tracer(0)

snake = Snake()


def restart_game():
    snake.reset()
    food.reset()
    wall.clear_game_over_box()
    score_tab.reset_score()


wall.set_restart_callback(restart_game)

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onclick(wall.try_again)

while True:
    screen.update()
    time.sleep(0.12)

    if wall.game_over:
        continue

    snake.move()
    food.snake_food_collision(snake)
    wall.wall_collision(snake)
