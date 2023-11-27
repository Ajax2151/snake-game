from turtle import Turtle
import random
COLORS = ["chartreuse", "cyan", "turquoise", "yellow", "light sky blue", "spring green", "light green", "khaki",
          "pale goldenrod", "orange", "peach puff", "sandy brown", "red", "light coral", "light pink", "violet",
          "orchid", "lavender"]


class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color(random.choice(COLORS))
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        """Spawns new piece of food at random X and Y coordinates."""
        random_x = random.randint(-275, 275)
        random_y = random.randint(-275, 275)
        self.color(random.choice(COLORS))
        self.goto(random_x, random_y)