import turtle as t
xy = [(0,0),(-20,0),(-40,0)]
d = 20
u = 90
dn = 270
lt = 180
rt = 0

class Snake:
    def __init__(self):
        self.all = []
        self.crsn()
        self.hd = self.all[0]
    def crsn(self):
        for i in xy:
            self.adseg(i)
    def adseg(self, ps):
        tu = t.Turtle(shape="turtle")
        tu.color("white")
        tu.penup()
        tu.goto(ps)
        self.all.append(tu)
    def rstsn(self):
        for z in self.all:
            z.goto(1000,1000)
        self.all.clear()
        self.crsn()
        self.hd = self.all[0]

    def extnd(self):
        self.adseg(self.all[-1].position())

    def mv(self):
        for i in range(len(self.all) - 1, 0, -1):
            nx = self.all[i - 1].xcor()
            ny = self.all[i - 1].ycor()
            self.all[i].goto(nx, ny)
        self.all[0].forward(d)

    def up(self):
        if self.hd.heading() != dn:
            self.hd.setheading(u)
    def down(self):
        if self.hd.heading() != u:
            self.hd.setheading(dn)
    def left(self):
        if self.hd.heading() != rt:
            self.hd.setheading(lt)
    def right(self):
        if self.hd.heading() != lt:
            self.hd.setheading(rt)
