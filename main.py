import turtle as t
import time
from snake import Snake
from food import Food
from score import scr
s = t.Screen()
s.setup(width=600, height=600)
s.bgcolor("black")
s.title("Aravind's Snake Game")
s.tracer(0)

sk = Snake()
fd = Food()
sr = scr()

s.listen()
s.onkey(sk.up,"Up")
s.onkey(sk.down,"Down")
s.onkey(sk.left,"Left")
s.onkey(sk.right,"Right")



end = False
while not end:
    s.update()
    time.sleep(0.1)
    sk.mv()
    if sk.hd.distance(fd) < 15:
        fd.rfh()
        sk.extnd()
        sr.inc()
    if sk.hd.xcor() > 280 or sk.hd.xcor() < -280 or sk.hd.ycor() > 280 or sk.hd.ycor() < -280 :
        sr.rst()
        sk.rstsn()
    for sg in sk.all[1:]:
        if sk.hd.distance(sg) < 10 :
            sr.rst()
            sk.rstsn()








s.exitonclick()