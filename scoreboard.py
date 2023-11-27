from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier New", 20, "normal")
GAME_OVER_FONT = ("Courier New", 32, "bold")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.show_score()

    def show_score(self):
        """Prints scoreboard at top center of screen"""
        self.hideturtle()
        self.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)
        self.penup()
        self.setpos(0, 265)
        self.color("white")

    # Update scoreboard
    def update_score(self):
        """Clears old score and refreshes scoreboard with new score"""
        self.clear()
        self.score += 1
        self.show_score()

    def game_over(self):
        """Prints game over message and displays at center of screen"""
        self.hideturtle()
        self.penup()
        self.home()
        self.color("red")
        self.write("GAME OVER", align=ALIGNMENT, font=GAME_OVER_FONT)
