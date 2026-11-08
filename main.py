from turtle import Screen

from food import Food
from scoreboard import Scoreboard
from snake import Snake
from theme import ACCENT, BACKGROUND, BOARD_HALF, DANGER, WINDOW_HEIGHT, WINDOW_WIDTH
from ui import Overlay, draw_board, register_shapes

FOOD_HIT_DISTANCE = 15
GAME_SPEED_MS = 100

# Game states
START, PLAYING, PAUSED, GAME_OVER = "start", "playing", "paused", "game_over"

screen = Screen()
screen.setup(width=WINDOW_WIDTH, height=WINDOW_HEIGHT)
screen.bgcolor(BACKGROUND)
screen.title("Snake")
screen.tracer(0)
register_shapes(screen)

# Draw the board first so the snake and food are drawn on top of it.
draw_board()
snake = Snake()
food = Food(snake.segments)
score_board = Scoreboard()
overlay = Overlay()
state = START


def show_pieces(visible):
    """Hide the snake and food behind an overlay (turtles are always drawn above text)."""
    snake.set_visible(visible)
    food.showturtle() if visible else food.hideturtle()


def show_start_screen():
    show_pieces(False)
    overlay.show("READY?", "Eat apples, grow longer.", "Don't hit the walls or yourself.",
                 "Press Space to start", title_color=ACCENT)


def on_space():
    global state
    if state in (START, PAUSED):
        state = PLAYING
        overlay.hide()
        show_pieces(True)
    elif state == PLAYING:
        state = PAUSED
        show_pieces(False)
        overlay.show("PAUSED", "Press Space to resume")
    elif state == GAME_OVER:
        score_board.reset_score()
        snake.reset()
        food.refresh(snake.segments)
        state = PLAYING
        overlay.hide()
        show_pieces(True)
    screen.update()


def game_over():
    global state
    state = GAME_OVER
    show_pieces(False)
    result = "New best score!" if score_board.is_new_best() else f"Best: {score_board.high_score}"
    overlay.show("GAME OVER", f"Score: {score_board.score}   ·   {result}",
                 "Press Space to play again", title_color=DANGER)
    screen.update()


def game_loop():
    if state == PLAYING:
        snake.move()
        food.pulse()

        # Detect collision with food
        if snake.head.distance(food) < FOOD_HIT_DISTANCE:
            snake.extend()
            food.refresh(snake.segments)
            score_board.increase_score()

        # Detect collision with wall or tail
        if snake.hit_wall(BOARD_HALF) or snake.hit_tail():
            game_over()

        screen.update()
    screen.ontimer(game_loop, GAME_SPEED_MS)


screen.listen()
for keys, action in (
    (("Up", "w", "W"), snake.up),
    (("Down", "s", "S"), snake.down),
    (("Left", "a", "A"), snake.left),
    (("Right", "d", "D"), snake.right),
    (("space",), on_space),
):
    for key in keys:
        screen.onkey(action, key)

show_start_screen()
screen.update()
game_loop()
screen.mainloop()
