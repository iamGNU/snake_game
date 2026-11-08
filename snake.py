from turtle import Turtle

from theme import SNAKE_BODY_END, SNAKE_BODY_START

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
TAIL_HIT_DISTANCE = 10


def blend(start_hex, end_hex, t):
    """Mix two '#rrggbb' colours; t=0 gives start, t=1 gives end."""
    start = [int(start_hex[i:i + 2], 16) for i in (1, 3, 5)]
    end = [int(end_hex[i:i + 2], 16) for i in (1, 3, 5)]
    return "#" + "".join(f"{round(s + (e - s) * t):02x}" for s, e in zip(start, end))


class Snake:
    def __init__(self):
        self.segments = []
        self.spare_segments = []  # hidden segments kept for reuse after a reset
        self.create_snake()

    def create_snake(self):
        """Create initial 3 segment body snake"""
        for position in STARTING_POSITIONS:
            self.add_segment(position)
        self.head = self.segments[0]
        self.head.setheading(RIGHT)
        # Direction the snake last moved in, and the one requested for the next move.
        self.direction = RIGHT
        self.next_direction = RIGHT
        self.restyle()

    def add_segment(self, position):
        if self.spare_segments:
            segment = self.spare_segments.pop()
        else:
            segment = Turtle()
            segment.penup()
        segment.goto(position)
        segment.showturtle()
        self.segments.append(segment)

    def restyle(self):
        """Give the head its face and shade the body from bright green to dark at the tail."""
        body = self.segments[1:]
        self.segments[0].shape("snake_head")
        for i, segment in enumerate(body):
            segment.shape("snake_body")
            segment.color(blend(SNAKE_BODY_START, SNAKE_BODY_END, i / max(len(body) - 1, 1)))

    def extend(self):
        """Adds new segment to snake"""
        self.add_segment(self.segments[-1].position())
        self.restyle()

    def move(self):
        for i in range(len(self.segments) - 1, 0, -1):
            self.segments[i].goto(self.segments[i - 1].position())
        self.head.setheading(self.next_direction)
        self.direction = self.next_direction
        self.head.forward(MOVE_DISTANCE)

    def turn(self, new_direction):
        """Queue a turn, ignoring a 180° reversal relative to the last move.

        Checking against the last *moved* direction (not the current heading)
        stops two quick key presses within one tick from reversing the snake.
        """
        if (new_direction - self.direction) % 360 != 180:
            self.next_direction = new_direction

    def up(self):
        self.turn(UP)

    def down(self):
        self.turn(DOWN)

    def left(self):
        self.turn(LEFT)

    def right(self):
        self.turn(RIGHT)

    def hit_wall(self, limit):
        return abs(self.head.xcor()) > limit or abs(self.head.ycor()) > limit

    def hit_tail(self):
        return any(self.head.distance(segment) < TAIL_HIT_DISTANCE for segment in self.segments[1:])

    def set_visible(self, visible):
        for segment in self.segments:
            segment.showturtle() if visible else segment.hideturtle()

    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.spare_segments.extend(self.segments)
        self.segments.clear()
        self.create_snake()
