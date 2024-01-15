import time
import turtle
from turtle import Turtle, Screen
import random

# window = Screen()
# window.setup(600, 600)

# snake = []  # each item in the "snake" list is a Turtle object
# x_offset = 0
# for i in range(3):
#
#     new_snake_body = turtle.Turtle(shape="square")
#     new_snake_body.penup()
#     new_snake_body.setposition(x_offset, 0)
#     x_offset -= 20
#     snake.append(new_snake_body)
#
#
# is_game_running = True
# while is_game_running:
#     window.update()
#     time.sleep(0.1)
#
#     for segment_number in range(len(snake) - 1, 0, -1):
#         new_x_coord = snake[segment_number - 1].xcor()
#         new_y_coord = snake[segment_number - 1].ycor()
#         snake[segment_number].goto(new_x_coord, new_y_coord)
#     snake[0].forward(20)

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 30

class Snake:

    def __init__(self):
        self.big_boi_snake = []  # each index is a turtle.Turtle() object
        self.create_snake()
        self.head = self.big_boi_snake[0]  # need to have a snake created before we can access [0]

    def create_snake(self):
        for position in STARTING_POSITIONS:  # creates a new snake body at each position in STARTING_POSITIONS
            new_snake_body = turtle.Turtle(shape="square")
            new_snake_body.color("white")
            new_snake_body.penup()
            new_snake_body.goto(position)
            self.big_boi_snake.append(new_snake_body)

    def move(self):
        for segment_number in range(len(self.big_boi_snake) - 1, 0, -1):  # creates a range with the starting value of length of big_boi_snake - 1
            new_x_coord = self.big_boi_snake[segment_number - 1].xcor()
            new_y_coord = self.big_boi_snake[segment_number - 1].ycor()
            self.big_boi_snake[segment_number].goto(new_x_coord, new_y_coord)
        self.big_boi_snake[0].forward(MOVE_DISTANCE)

    def up(self):
        self.head.setheading(90)

    def down(self):
        self.head.setheading(270)

    def left(self):
        self.head.setheading(180)

    def right(self):
        self.head.setheading(0)

