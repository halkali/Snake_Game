from turtle import Turtle
ALIGN = "center"
FONT = ("arial", 20, "normal")

class score_board(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        with open('snake_score.txt') as file:
            self.high_score = file.read()
        self.color("white")
        self.hideturtle()
        self.penup()
        self.speed("fastest")
        self.goto(0, 320)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score}  High Score:{self.high_score}", align=ALIGN, font=FONT, move=False)

    def reset_(self):
        if self.score > int(self.high_score):
            self.high_score = self.score
            with open('snake_score.txt', mode="w") as file:
                file.write(str(self.high_score))

        self.score = 0
        self.update_scoreboard()


    #def game_over(self):
        #self.goto(0,0)
        #self.write("GAME OVER!", align=ALIGN, font=FONT, move=False)

    def add(self):
        self.score += 1
        self.update_scoreboard()



