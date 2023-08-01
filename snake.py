from turtle import Turtle,Screen
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
DISTANCE = 20
LEFT = 180
RIGHT = 0
UP = 90
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for self.position in STARTING_POSITIONS:
            self.add(self.position)

    def add(self,position):
        self.new = Turtle("square")
        self.new.color("white")
        self.new.penup()
        self.new.goto(position)
        self.new.speed("fastest")
        self.segments.append(self.new)

    def reset_(self):
        for seg in self.segments:
            seg.goto(1000,1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
    def extend(self):
        self.add(self.segments[-1].position())



    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            x = self.segments[i - 1].xcor()
            y = self.segments[i - 1].ycor()
            self.segments[i].goto(x, y)
        self.head.forward(DISTANCE)

    def turn_left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
    def turn_right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
    def turn_down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
    def turn_up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)



