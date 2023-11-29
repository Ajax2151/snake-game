from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        with open("data.txt") as data:
            self.high_score = int(data.read())
        self.show_score()

    def show_score(self):
        """Prints scoreboard at top center of screen"""
        self.hideturtle()
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)
        self.penup()
        self.setpos(0, 265)
        self.color("white")

    # Update scoreboard
    def update_score(self):
        """Clears old score and refreshes scoreboard with new score"""
        self.clear()
        self.score += 1
        self.show_score()

    def reset_board(self):
        """Resets player score to zero, stores high scores to data file"""
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{self.high_score}")
        self.score = 0
        self.update_score()
