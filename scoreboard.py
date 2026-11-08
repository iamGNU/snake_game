from pathlib import Path
from turtle import Turtle

from theme import BOARD_HALF, HUD_FONT, HUD_Y, MUTED, TEXT

# Stored next to this file so the game works no matter which folder it's run from.
HIGH_SCORE_FILE = Path(__file__).with_name("data.txt")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.load_high_score()
        self.best_at_start = self.high_score
        self.hideturtle()
        self.penup()
        self.update_scoreboard()

    @staticmethod
    def load_high_score():
        try:
            return int(HIGH_SCORE_FILE.read_text().strip())
        except (FileNotFoundError, ValueError):
            return 0

    def save_high_score(self):
        HIGH_SCORE_FILE.write_text(str(self.high_score))

    def write_stat(self, x, label, value):
        """Write a muted label followed by its value, e.g. 'SCORE 7'."""
        self.goto(x, HUD_Y + 4)
        self.color(MUTED)
        self.write(f"{label} ", align="left", font=HUD_FONT, move=True)
        self.color(TEXT)
        self.write(str(value), align="left", font=HUD_FONT)

    def update_scoreboard(self):
        self.clear()
        self.write_stat(BOARD_HALF - 210, "SCORE", self.score)
        self.write_stat(BOARD_HALF - 90, "BEST", self.high_score)

    def increase_score(self):
        self.score += 1
        if self.score > self.high_score:
            # Save straight away so a new high score survives closing the window mid-game.
            self.high_score = self.score
            self.save_high_score()
        self.update_scoreboard()

    def is_new_best(self):
        return self.score > self.best_at_start

    def reset_score(self):
        self.score = 0
        self.best_at_start = self.high_score
        self.update_scoreboard()
