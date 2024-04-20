from turtle import Turtle

#Define alignment and font of the scoreboard
ALINGMENT="center"
FONT=("Arial", 22, "normal")
class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score=0
        with open("data.txt") as data:
            self.high_score=int(data.read())
        self.goto(0,270)
        self.penup()
        self.color("white")
        self.hideturtle()
        self.uptade_scoreboard()

    def uptade_scoreboard(self):
        self.clear()
        self.write(f"Score:{self.score} High Score:{self.high_score}",align=ALINGMENT, font=FONT)


    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("data.txt",write="w") as data:
                data.write(f"{self.high_score}")

        self.score = 0
        self.uptade_scoreboard()

    #def game_over(self):
       # self.goto(0,0)
       # self.write("Game over!",align=ALINGMENT,font=FONT)
    def increase_score(self):
        self.score+=1
        self.uptade_scoreboard()

