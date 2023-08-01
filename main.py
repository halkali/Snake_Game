import time
import turtle
from turtle import Turtle, Screen
from random import randint
from snake import Snake
from food import Food
from scoreboard import score_board
snake = Snake()

screen = Screen()
screen.listen()
screen.onkey(key="Left", fun=snake.turn_left)
screen.onkey(key="Right", fun=snake.turn_right)
screen.onkey(key="Up", fun=snake.turn_up)
screen.onkey(key="Down", fun=snake.turn_down)


screen.bgcolor("black")
screen.setup(height=700, width=700)
screen.title("Snake Game")
screen.tracer(0)
food = Food()

board = score_board()



game_is_on = True

while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move()
    for i in snake.segments[1:]:
        if snake.head.distance(i.pos()) <10:
            board.reset_()
            snake.reset_()
    if snake.head.distance(food) < 15:
        print("nomnomnom")
        food.refresh()
        board.add()
        snake.extend()
    if (snake.head.xcor() < -340 or snake.head.ycor() < -340) or (snake.head.xcor() > 340 or snake.head.ycor() > 340):
        board.reset_()
        snake.reset_()

















































screen.exitonclick()