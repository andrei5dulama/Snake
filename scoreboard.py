from turtle import Turtle
ALIGNMENT = 'center'
FONT = ('Arial', 24, 'normal')

class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.color('white')
        self.score = 0
        with open('data.txt') as data:
            self.high_score = int(data.read())
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(arg=f'Score: {self.score} High Score: {self.high_score}', align=ALIGNMENT, font=FONT)

    def reset_self(self):
        if self.score > self.high_score:
            self.high_score = self.score
            self.score = 0
            self.update_scoreboard()
            with open('data.txt') as data:
                data.write(self.high_score)


    def game_over(self):
        self.goto(0, 0)
        self.write(arg='Game Over', align='center', font=('Arial', 50, 'normal'))
    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
