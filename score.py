from turtle import Turtle
aln = "center"
fnt = ("Courier", 20, "normal")
class scr(Turtle):
    def __init__(self):
        super().__init__()
        self.op = 0
        # with open("/Users/ARAVINDVAS/PycharmProjects/data2.txt") as fle:
        # with open("../../PycharmProjects/data2.txt") as fle:
        with open("data.txt") as fle:
            self.hs = int(fle.read())
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.upd()
    def upd(self):
        self.clear()
        self.write(f"Score: {self.op} Highest Score: {self.hs}", align=aln, font=fnt)
    def rst(self):
        if self.op > self.hs:
            self.hs = self.op
            # with open("/Users/ARAVINDVAS/PycharmProjects/data2.txt", mode="w") as fl2:
            # with open("../../PycharmProjects/data2.txt", mode="w") as fl2:
            with open("data.txt", mode="w") as fl2:
                fl2.write(f"{self.hs}")
        self.op = 0
        self.upd()
    # def gmr(self):
    #     self.goto(0,0)
    #     self.write(f"GAME OVER", align=aln, font=fnt)
    def inc(self):
        self.op += 1
        self.upd()
