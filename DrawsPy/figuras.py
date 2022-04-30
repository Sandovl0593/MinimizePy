from turtle import *
from math import *
# Tmanaño del monitor
# from screeninfo import get_monitors
# for m in get_monitors():
#     print(str(m))

root = Screen()
hideturtle()
root.bgcolor("black")
root.setup(1000, 580, -400)

def moon():
    rmay = 140
    angulomen = 180
    rmen = 110
    penup()
    goto(0, -50)
    pendown()
    begin_fill()
    left(25)
    color("white","white")
    pensize(10)
    speed(2)
    circle(rmen, -angulomen)
    left(40)
    angulomay = round(acos(-(((2*rmen)**2 - rmay**2 - rmay**2)/(2*rmay*rmay)))*180/pi)-1
    circle(rmay, angulomay)
    end_fill()
    root.mainloop()

moon()