"""Static drawing for the game: custom shapes, the board, and message overlays."""
import math
from turtle import Shape, Turtle

from theme import (
    ACCENT, BOARD_DARK, BOARD_HALF, BOARD_LIGHT, BORDER, CELL_SIZE, EYE, FOOD, FOOD_LEAF,
    FOOD_SHINE, HINT_FONT, HINT_Y, HUD_Y, MUTED, OVERLAY_TEXT_FONT, OVERLAY_TITLE_FONT,
    PANEL, PUPIL, SNAKE_HEAD, TEXT, TITLE_FONT,
)


# --- Shape helpers -------------------------------------------------------------
# Turtle draws a custom shape as if it were facing up (heading 90), so +y is "forward".

def rounded_rect(half_w, half_h, radius, steps=4):
    """Points of a rectangle centred on (0, 0) with rounded corners."""
    corners = [
        (half_w - radius, half_h - radius, 0),
        (-half_w + radius, half_h - radius, 90),
        (-half_w + radius, -half_h + radius, 180),
        (half_w - radius, -half_h + radius, 270),
    ]
    points = []
    for cx, cy, start in corners:
        for i in range(steps + 1):
            angle = math.radians(start + 90 * i / steps)
            points.append((cx + radius * math.cos(angle), cy + radius * math.sin(angle)))
    return tuple(points)


def ellipse(cx, cy, rx, ry, tilt=0, steps=16):
    tilt = math.radians(tilt)
    points = []
    for i in range(steps):
        a = 2 * math.pi * i / steps
        x, y = rx * math.cos(a), ry * math.sin(a)
        points.append((cx + x * math.cos(tilt) - y * math.sin(tilt),
                       cy + x * math.sin(tilt) + y * math.cos(tilt)))
    return tuple(points)


def register_shapes(screen):
    screen.register_shape("snake_body", rounded_rect(9, 9, 4))

    head = Shape("compound")
    head.addcomponent(rounded_rect(10, 10, 5), SNAKE_HEAD, SNAKE_HEAD)
    for side in (-1, 1):
        head.addcomponent(ellipse(5 * side, 3, 3.2, 3.2), EYE, EYE)
        head.addcomponent(ellipse(5 * side, 4.5, 1.6, 1.6), PUPIL, PUPIL)
    screen.register_shape("snake_head", head)

    apple = Shape("compound")
    apple.addcomponent(ellipse(0, -1, 7.5, 7.5), FOOD, FOOD)
    apple.addcomponent(ellipse(-3, 2, 1.8, 1.8), FOOD_SHINE, FOOD_SHINE)
    apple.addcomponent(ellipse(3, 7.5, 3.5, 1.8, tilt=30), FOOD_LEAF, FOOD_LEAF)
    screen.register_shape("apple", apple)


# --- Drawing -------------------------------------------------------------------

def _pen():
    pen = Turtle()
    pen.hideturtle()
    pen.penup()
    pen.speed(0)
    return pen


def _fill_polygon(pen, points, fill, outline, width=1):
    pen.goto(points[0])
    pen.color(outline, fill)
    pen.pensize(width)
    pen.begin_fill()
    pen.pendown()
    for point in points[1:] + points[:1]:
        pen.goto(point)
    pen.penup()
    pen.end_fill()


def draw_board():
    """Draw the checkered playing field, its border, the title and the controls hint."""
    pen = _pen()
    edge = BOARD_HALF + 3
    _fill_polygon(pen, rounded_rect(edge, edge, 6), BOARD_LIGHT, BORDER, width=3)

    pen.shape("square")
    pen.color(BOARD_DARK)
    cells = range(-BOARD_HALF + CELL_SIZE // 2, BOARD_HALF, CELL_SIZE)
    for i, x in enumerate(cells):
        for j, y in enumerate(cells):
            if (i + j) % 2:
                pen.goto(x, y)
                pen.stamp()

    pen.goto(-BOARD_HALF, HUD_Y)
    pen.color(ACCENT)
    pen.write("SNAKE", align="left", font=TITLE_FONT)
    pen.goto(0, HINT_Y)
    pen.color(MUTED)
    pen.write("Arrows / WASD  move        Space  pause", align="center", font=HINT_FONT)


class Overlay:
    """A panel in the middle of the board with a title and a line or two of text."""

    def __init__(self):
        self.pen = _pen()

    def show(self, title, *lines, title_color=TEXT):
        self.hide()
        height = 70 + 26 * len(lines)
        _fill_polygon(self.pen, rounded_rect(190, height / 2, 12), PANEL, title_color, width=2)
        y = height / 2 - 52
        self.pen.goto(0, y)
        self.pen.color(title_color)
        self.pen.write(title, align="center", font=OVERLAY_TITLE_FONT)
        for i, line in enumerate(lines):
            y -= 28
            self.pen.goto(0, y)
            # The last line is the call to action, so it stands out more.
            self.pen.color(TEXT if i == len(lines) - 1 else MUTED)
            self.pen.write(line, align="center", font=OVERLAY_TEXT_FONT)

    def hide(self):
        self.pen.clear()
