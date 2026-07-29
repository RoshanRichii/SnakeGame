# snake constants
from turtle import Turtle

START_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20


class Snake:
    def __init__(self):
        self.segments = []
        self.eye = None
        self.create_snake()

    def create_snake(self):
        for index, position in enumerate(START_POSITIONS):
            new_segment = Turtle("square")
            new_segment.penup()
            new_segment.goto(position)

            if index == 0:
                new_segment.color("lime")
                new_segment.shapesize(stretch_wid=1.0, stretch_len=1.0)
            elif index == len(START_POSITIONS) - 1:
                new_segment.color("lightgreen")
                new_segment.shape("triangle")
                new_segment.shapesize(stretch_wid=1.0, stretch_len=1.0)
            else:
                new_segment.color("green")
                new_segment.shapesize(stretch_wid=0.9, stretch_len=0.9)

            self.segments.append(new_segment)

        self.create_eye()

    def create_eye(self):
        if self.eye is not None:
            self.eye.hideturtle()

        self.eye = Turtle("circle")
        self.eye.color("black")
        self.eye.penup()
        self.eye.shapesize(stretch_wid=0.25, stretch_len=0.25)
        self.update_eye()

    def update_eye(self):
        head = self.segments[0]
        heading = head.heading()

        if heading == 0:
            self.eye.goto(head.xcor() + 4, head.ycor() + 2)
        elif heading == 90:
            self.eye.goto(head.xcor() + 2, head.ycor() + 4)
        elif heading == 180:
            self.eye.goto(head.xcor() - 4, head.ycor() + 2)
        elif heading == 270:
            self.eye.goto(head.xcor() + 2, head.ycor() - 4)
        else:
            self.eye.goto(head.xcor() + 3, head.ycor() + 3)

    def move(self):
        for segment_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[segment_num - 1].xcor()
            new_y = self.segments[segment_num - 1].ycor()
            self.segments[segment_num].goto(new_x, new_y)
            self.segments[segment_num].setheading(self.segments[segment_num - 1].heading())

        self.segments[0].forward(MOVE_DISTANCE)
        self.update_eye()

    def up(self):
        if self.segments[0].heading() != 270:
            self.segments[0].setheading(90)
            self.update_eye()

    def down(self):
        if self.segments[0].heading() != 90:
            self.segments[0].setheading(270)
            self.update_eye()

    def left(self):
        if self.segments[0].heading() != 0:
            self.segments[0].setheading(180)
            self.update_eye()

    def right(self):
        if self.segments[0].heading() != 180:
            self.segments[0].setheading(0)
            self.update_eye()

    def reset(self):
        for segment in self.segments:
            segment.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()

    def extend(self):
        new_segment = Turtle("triangle")
        new_segment.color("lightgreen")
        new_segment.penup()
        last_segment_position = self.segments[-1].position()
        new_segment.goto(last_segment_position)
        new_segment.setheading(self.segments[-1].heading())
        self.segments.append(new_segment)
        self.update_eye()
