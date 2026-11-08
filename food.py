from turtle import Turtle
import random

from theme import BOARD_HALF, CELL_SIZE

GRID_STEPS = (BOARD_HALF - CELL_SIZE // 2) // CELL_SIZE  # food spawns on the snake's grid
OVERLAP_DISTANCE = 15
PULSE_SIZES = (1.0, 1.0, 1.12, 1.12)  # gentle "breathing" so the food catches the eye


class Food(Turtle):
    def __init__(self, occupied=()):
        super().__init__()
        self.shape("apple")
        self.setheading(90)  # draw the apple upright, leaf on top
        self.penup()
        self.pulse_step = 0
        self.refresh(occupied)

    def refresh(self, occupied=()):
        """Move the food to a random grid position not covered by any turtle in `occupied`."""
        while True:
            x = random.randint(-GRID_STEPS, GRID_STEPS) * CELL_SIZE
            y = random.randint(-GRID_STEPS, GRID_STEPS) * CELL_SIZE
            if all(segment.distance(x, y) >= OVERLAP_DISTANCE for segment in occupied):
                break
        self.goto(x, y)

    def pulse(self):
        self.pulse_step = (self.pulse_step + 1) % len(PULSE_SIZES)
        size = PULSE_SIZES[self.pulse_step]
        self.shapesize(size, size)
