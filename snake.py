from turtle import Turtle
STARTING_POSITIONS = starting_positions = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]

    def create_snake(self):
        """Creates beginning snake with three segments"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """Create new snake segments"""
        new_segment = Turtle("square")
        new_segment.color("white")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def reset_snake(self):
        """Resets snake to base 3 segments after running into wall or tail"""
        for seg in self.segments:
            seg.goto(1000, 1000)
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]

    def extend(self):
        """Add a new segment to the snake"""
        self.add_segment(self.segments[-1].position())

    def move(self):
        """Moves snake body - third segment moves to position of second, second moves to position of first,
        first moves 20 forward in designated heading"""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)

    def up(self):
        """Sets snake heading to top of screen if snake is not moving towards bottom of screen"""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            self.move()

    def down(self):
        """Sets snake heading to bottom of screen if snake is not moving towards top of screen"""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            self.move()

    def left(self):
        """Sets snake heading to left side of screen if snake is not going right"""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            self.move()

    def right(self):
        """Sets snake heading to right side of screen if snake is not going left"""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            self.move()
